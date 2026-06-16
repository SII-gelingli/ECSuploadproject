"""
ElectrochemAgent: ReAct loop supporting both Anthropic and OpenAI-compatible backends.

Manages conversation history and iteratively calls tools until the LLM
produces a final text response.
"""
import os
import re
import json
from typing import Dict, List, Optional, Any

import httpx

from agent.prompts import SYSTEM_PROMPT, TOOL_SCHEMAS, get_openai_tool_schemas
from agent.tools import ToolExecutor
from config import AgentConfig


class ElectrochemAgent:
    """
    ReAct agent that uses LLM tool_use to orchestrate
    electrochemical condition recommendation.

    Supports two backends:
      - "anthropic" (default): Anthropic Claude API
      - "openai": Any OpenAI-compatible endpoint (e.g. vLLM)

    Usage:
        agent = ElectrochemAgent(config, model_manager, retriever)
        response = agent.chat("Recommend conditions for CC(=O)c1ccccc1>>CC(O)c1ccccc1")
    """

    def __init__(self, config: AgentConfig, model_manager, retriever=None, mechanism_retriever=None):
        self.config = config
        self.backend = getattr(config, "backend", "openai")

        # Build httpx client with proxy support and timeout
        timeout_ms = int(os.environ.get("API_TIMEOUT_MS", "600000"))
        timeout = httpx.Timeout(timeout_ms / 1000.0, connect=30.0)
        proxy_url = (os.environ.get("HTTPS_PROXY")
                     or os.environ.get("https_proxy")
                     or os.environ.get("HTTP_PROXY")
                     or os.environ.get("http_proxy"))
        http_client = httpx.Client(timeout=timeout, proxy=proxy_url) if proxy_url else httpx.Client(timeout=timeout)

        if self.backend == "openai":
            from openai import OpenAI
            base_url = config.base_url or "http://localhost:8000/v1"
            # OpenAI SDK 2.x 不会自动追加 /v1, 必须手动加
            if base_url and not base_url.rstrip('/').endswith('/v1'):
                base_url = base_url.rstrip('/') + '/v1'
            self.client = OpenAI(
                api_key=config.api_key or "EMPTY",
                base_url=base_url,
                http_client=http_client,
            )
        else:
            from anthropic import Anthropic
            client_kwargs = {
                "api_key": config.api_key,
                "http_client": http_client,
            }
            if config.base_url:
                client_kwargs["base_url"] = config.base_url
            self.client = Anthropic(**client_kwargs)

        self.tool_executor = ToolExecutor(model_manager, retriever, mechanism_retriever)
        self.conversation: List[Dict] = []

    def reset(self):
        """Clear conversation history."""
        self.conversation = []
        self.tool_executor._fp_cache.clear()

    # ── LLM call dispatch ─────────────────────────────────────────

    def _call_llm(self):
        """Dispatch to the appropriate backend."""
        if self.backend == "openai":
            return self._call_openai()
        return self._call_anthropic()

    def _call_anthropic(self):
        """Make a single Anthropic Claude API call with tools."""
        return self.client.messages.create(
            model=self.config.model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            system=SYSTEM_PROMPT,
            tools=TOOL_SCHEMAS,
            messages=self.conversation,
        )

    def _call_openai(self):
        """Make a single OpenAI-compatible API call with tools."""
        # Build messages: system prompt first, then conversation
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(self.conversation)

        return self.client.chat.completions.create(
            model=self.config.model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            messages=messages,
            tools=get_openai_tool_schemas(),
        )

    # ── Thinking-tag helper ─────────────────────────────────────

    _THINK_RE = re.compile(r"<think>.*?</think>\s*", re.DOTALL)

    @staticmethod
    def _strip_thinking(text: str) -> str:
        """Remove <think>...</think> blocks from model output (e.g. Qwen3.5)."""
        return ElectrochemAgent._THINK_RE.sub("", text).strip()

    # ── Response parsing ──────────────────────────────────────────

    def _parse_response(self, response):
        """
        Parse LLM response into a unified format.

        Returns:
            (text_parts, tool_uses, raw_message, stop_reason)
            - text_parts: list of str
            - tool_uses: list of dict {"id", "name", "input"}
            - raw_message: object to store in conversation history
            - stop_reason: str or None
        """
        if self.backend == "openai":
            return self._parse_openai_response(response)
        return self._parse_anthropic_response(response)

    def _parse_anthropic_response(self, response):
        text_parts = []
        tool_uses = []
        for block in response.content:
            if block.type == "text":
                text_parts.append(block.text)
            elif block.type == "tool_use":
                tool_uses.append({
                    "id": block.id,
                    "name": block.name,
                    "input": block.input,
                })
        raw_message = response.content
        stop_reason = response.stop_reason
        return text_parts, tool_uses, raw_message, stop_reason

    def _parse_openai_response(self, response):
        choice = response.choices[0]
        message = choice.message

        text_parts = []
        if message.content:
            cleaned = self._strip_thinking(message.content)
            if cleaned:
                text_parts.append(cleaned)

        tool_uses = []
        if message.tool_calls:
            for tc in message.tool_calls:
                try:
                    args = json.loads(tc.function.arguments)
                except (json.JSONDecodeError, TypeError):
                    args = {}
                tool_uses.append({
                    "id": tc.id,
                    "name": tc.function.name,
                    "input": args,
                })

        # For OpenAI, we store the full message dict so tool_calls are preserved
        raw_message = {
            "role": "assistant",
            "content": message.content or "",
        }
        if message.tool_calls:
            raw_message["tool_calls"] = [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    },
                }
                for tc in message.tool_calls
            ]

        stop_reason = choice.finish_reason  # "stop" or "tool_calls"
        return text_parts, tool_uses, raw_message, stop_reason

    # ── Tool result formatting ────────────────────────────────────

    def _format_tool_results(self, tool_results_data):
        """
        Format tool results for the conversation history.

        Args:
            tool_results_data: list of dict {"id", "content"}

        Returns:
            For Anthropic: single user message with tool_result content blocks
            For OpenAI: list of tool messages (one per tool call)
        """
        if self.backend == "openai":
            messages = []
            for tr in tool_results_data:
                messages.append({
                    "role": "tool",
                    "tool_call_id": tr["id"],
                    "content": tr["content"],
                })
            return messages
        else:
            # Anthropic format: single user message with tool_result blocks
            return [{
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": tr["id"],
                        "content": tr["content"],
                    }
                    for tr in tool_results_data
                ],
            }]

    # ── Conversation history helpers ──────────────────────────────

    def _append_assistant(self, raw_message):
        """Append assistant response to conversation."""
        if self.backend == "openai":
            # raw_message is already a dict for OpenAI
            self.conversation.append(raw_message)
        else:
            # Anthropic: raw_message is response.content
            self.conversation.append({"role": "assistant", "content": raw_message})

    def _append_tool_results(self, formatted):
        """Append tool results to conversation."""
        if self.backend == "openai":
            # OpenAI: each tool result is a separate message
            self.conversation.extend(formatted)
        else:
            # Anthropic: single user message with all tool results
            self.conversation.extend(formatted)

    # ── Main chat loop ────────────────────────────────────────────

    def chat(self, user_message: str, display_callback=None) -> str:
        """
        Send a user message and run the ReAct loop until a final text response.

        Args:
            user_message: The user's input text.
            display_callback: Optional callable(event_type, data) for live display.
                event_type: 'thinking', 'tool_call', 'tool_result', 'response'

        Returns:
            The agent's final text response.
        """
        self.conversation.append({"role": "user", "content": user_message})

        for round_num in range(self.config.max_tool_rounds):
            response = self._call_llm()
            text_parts, tool_uses, raw_message, stop_reason = self._parse_response(response)

            # Add assistant message to conversation
            self._append_assistant(raw_message)

            # If no tool calls, we have the final response
            if not tool_uses:
                final_text = "\n".join(text_parts)
                if display_callback:
                    display_callback('response', final_text)
                return final_text

            # If stop_reason is "end_turn"/"stop" and there's text but also tool calls,
            # process the tool calls first
            anthropic_end = (stop_reason == "end_turn" and not tool_uses)
            openai_end = (stop_reason == "stop" and not tool_uses)
            if anthropic_end or openai_end:
                final_text = "\n".join(text_parts)
                if display_callback:
                    display_callback('response', final_text)
                return final_text

            # Display thinking text if any
            if text_parts and display_callback:
                display_callback('thinking', "\n".join(text_parts))

            # Execute each tool call and build tool_result data
            tool_results_data = []
            for tool_use in tool_uses:
                tool_name = tool_use["name"]
                tool_input = tool_use["input"]

                if display_callback:
                    display_callback('tool_call', {
                        'name': tool_name,
                        'input': tool_input,
                    })

                result_str = self.tool_executor.execute(tool_name, tool_input)

                # For draw_reaction, strip base64 from the result sent to LLM
                # (saves tokens) but keep full result for display
                display_result_str = result_str
                llm_result_str = result_str
                if tool_name == "draw_reaction":
                    try:
                        parsed = json.loads(result_str)
                        for img in parsed.get("images", []):
                            img.pop("image_base64", None)
                        llm_result_str = json.dumps(parsed, ensure_ascii=False)
                    except Exception:
                        pass

                if display_callback:
                    # 完整显示, 不截断
                    full_result = display_result_str if tool_name == "draw_reaction" else result_str
                    display_callback('tool_result', {
                        'name': tool_name,
                        'result': full_result,
                    })

                tool_results_data.append({
                    "id": tool_use["id"],
                    "content": llm_result_str,
                })

            # Add tool results to conversation
            formatted = self._format_tool_results(tool_results_data)
            self._append_tool_results(formatted)

        # Max rounds reached — ask LLM to summarize
        self.conversation.append({
            "role": "user",
            "content": (
                "You have reached the maximum number of tool calls. "
                "Please summarize your findings and provide your final recommendation "
                "based on the information gathered so far."
            ),
        })
        response = self._call_llm()
        text_parts, _, raw_message, _ = self._parse_response(response)
        final_text = "\n".join(text_parts)

        self._append_assistant(raw_message)

        if display_callback:
            display_callback('response', final_text)

        return final_text
