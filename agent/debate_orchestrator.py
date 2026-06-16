"""
DebateOrchestrator: 4-phase multi-model debate for electrochemical condition recommendation.

Phase 1: Independent recommendations (parallel — Claude with tools, GPT text-only)
Phase 2: Cross-critique (parallel)
Phase 3: Revision (parallel)
Phase 4: Final judgment (Gemini)

Uses ThreadPoolExecutor for parallel execution within each phase.
Graceful degradation: falls back to single-model if external models fail.
"""
import os
import logging
from dataclasses import dataclass, field
from typing import List, Optional, Callable
from concurrent.futures import ThreadPoolExecutor, as_completed

import httpx
from openai import OpenAI

from agent.debate_config import DebateConfig
from agent.debate_prompts import (
    RECOMMENDER_B_SYSTEM_PROMPT,
    CRITIC_SYSTEM_PROMPT,
    JUDGE_SYSTEM_PROMPT,
    build_recommender_b_message,
    build_critic_message,
    build_revision_message,
    build_judge_message,
)

logger = logging.getLogger(__name__)


@dataclass
class DebateResult:
    """Container for all debate phase outputs."""
    recommendation_a: str = ""           # Claude's original recommendation
    recommendation_b: str = ""           # GPT's original recommendation
    critique_of_a: Optional[str] = None  # GPT's critique of Claude's proposal
    critique_of_b: Optional[str] = None  # Claude's critique of GPT's proposal
    revision_a: Optional[str] = None     # Claude's revised proposal
    revision_b: Optional[str] = None     # GPT's revised proposal
    judgment: Optional[str] = None       # Gemini's final judgment
    final_answer: str = ""               # The answer shown to the user
    phases_completed: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)  # Error messages from failed phases


class DebateOrchestrator:
    """
    Orchestrates a 4-phase debate between Claude (Recommender A),
    GPT (Recommender B), and Gemini (Judge).
    """

    def __init__(self, agent, debate_config: DebateConfig):
        """
        Args:
            agent: An ElectrochemAgent instance (used for Phase 1 Claude recommendation).
            debate_config: DebateConfig with model names and API settings.
        """
        self.agent = agent
        self.config = debate_config

        # Build OpenAI-compatible client for GPT and Gemini calls
        # (also used for Claude text-only calls in Phase 2/3)
        proxy_url = (
            os.environ.get("HTTPS_PROXY")
            or os.environ.get("https_proxy")
            or os.environ.get("HTTP_PROXY")
            or os.environ.get("http_proxy")
        )
        timeout_ms = int(os.environ.get("API_TIMEOUT_MS", "600000"))
        http_client = httpx.Client(
            timeout=httpx.Timeout(timeout_ms / 1000.0, connect=30.0),
            proxy=proxy_url,
        ) if proxy_url else httpx.Client(
            timeout=httpx.Timeout(timeout_ms / 1000.0, connect=30.0),
        )

        # OpenAI SDK requires base_url to end with /v1
        raw_base = debate_config.base_url or os.environ.get("ANTHROPIC_BASE_URL", "")
        openai_base = raw_base.rstrip("/") + "/v1" if raw_base and not raw_base.rstrip("/").endswith("/v1") else raw_base

        self.openai_client = OpenAI(
            api_key=debate_config.api_key or os.environ.get("ANTHROPIC_API_KEY", ""),
            base_url=openai_base,
            http_client=http_client,
        )

    def run_debate(
        self,
        user_query: str,
        display_callback: Optional[Callable] = None,
    ) -> DebateResult:
        """
        Execute the full 4-phase debate.

        Args:
            user_query: The user's electrochemical reaction query.
            display_callback: Optional callable(event_type, data) for live display.
                event_type values: 'phase_start', 'phase_end', 'recommendation_a',
                'recommendation_b', 'critique', 'revision', 'judgment', 'error'

        Returns:
            DebateResult with all phase outputs and the final answer.
        """
        result = DebateResult()

        def _notify(event_type, data):
            if display_callback:
                try:
                    display_callback(event_type, data)
                except Exception:
                    pass

        # ── Phase 1: Independent Recommendations (parallel) ────────
        _notify("phase_start", "Phase 1: Independent Recommendations")

        rec_a = None
        rec_b = None

        with ThreadPoolExecutor(max_workers=2) as pool:
            future_a = pool.submit(self._get_recommendation_a, user_query)
            future_b = pool.submit(self._get_recommendation_b, user_query)

            try:
                rec_a = future_a.result(timeout=300)
                result.recommendation_a = rec_a
                _notify("recommendation_a", rec_a)
            except Exception as e:
                err = f"Recommender A (Claude) failed: {type(e).__name__}: {e}"
                logger.error("Phase 1: %s", err)
                result.errors.append(err)
                _notify("error", err)

            try:
                rec_b = future_b.result(timeout=300)
                result.recommendation_b = rec_b
                _notify("recommendation_b", rec_b)
            except Exception as e:
                err = f"Recommender B ({self.config.recommender_b_model}) failed: {type(e).__name__}: {e}"
                logger.error("Phase 1: %s", err)
                result.errors.append(err)
                _notify("error", err)

        result.phases_completed.append("phase1_recommendation")
        _notify("phase_end", "Phase 1 complete")

        # If both failed, return empty
        if not rec_a and not rec_b:
            result.final_answer = "Both recommenders failed. Please try again."
            return result

        # If only one succeeded, skip debate and return that recommendation
        if not rec_b:
            result.final_answer = rec_a
            return result
        if not rec_a:
            result.final_answer = rec_b
            return result

        # ── Phase 2: Cross-Critique (parallel) ─────────────────────
        _notify("phase_start", "Phase 2: Cross-Critique")

        critique_of_a = None  # GPT critiques Claude's proposal
        critique_of_b = None  # Claude critiques GPT's proposal

        with ThreadPoolExecutor(max_workers=2) as pool:
            # Claude (A) critiques GPT's proposal (B)
            future_cb = pool.submit(
                self._call_claude_text_only,
                CRITIC_SYSTEM_PROMPT,
                build_critic_message("A", rec_b, user_query),
                self.config.critic_max_tokens,
            )
            # GPT (B) critiques Claude's proposal (A)
            future_ca = pool.submit(
                self._call_openai_model,
                self.config.recommender_b_model,
                CRITIC_SYSTEM_PROMPT,
                build_critic_message("B", rec_a, user_query),
                self.config.critic_max_tokens,
            )

            try:
                critique_of_b = future_cb.result(timeout=180)
                result.critique_of_b = critique_of_b
                _notify("critique", {"by": "A", "of": "B", "text": critique_of_b})
            except Exception as e:
                err = f"Phase 2: Claude critique of B failed: {type(e).__name__}: {e}"
                logger.error(err)
                result.errors.append(err)
                _notify("error", err)

            try:
                critique_of_a = future_ca.result(timeout=180)
                result.critique_of_a = critique_of_a
                _notify("critique", {"by": "B", "of": "A", "text": critique_of_a})
            except Exception as e:
                err = f"Phase 2: GPT critique of A failed: {type(e).__name__}: {e}"
                logger.error(err)
                result.errors.append(err)
                _notify("error", err)

        result.phases_completed.append("phase2_critique")
        _notify("phase_end", "Phase 2 complete")

        # ── Phase 3: Revision (parallel) ───────────────────────────
        _notify("phase_start", "Phase 3: Revision")

        revision_a = None
        revision_b = None

        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = {}

            # Claude revises based on GPT's critique (if available)
            if critique_of_a:
                futures["revision_a"] = pool.submit(
                    self._call_claude_text_only,
                    RECOMMENDER_B_SYSTEM_PROMPT,  # reuse domain knowledge prompt
                    build_revision_message(rec_a, critique_of_a),
                    self.config.revision_max_tokens,
                )

            # GPT revises based on Claude's critique (if available)
            if critique_of_b:
                futures["revision_b"] = pool.submit(
                    self._call_openai_model,
                    self.config.recommender_b_model,
                    RECOMMENDER_B_SYSTEM_PROMPT,
                    build_revision_message(rec_b, critique_of_b),
                    self.config.revision_max_tokens,
                )

            if "revision_a" in futures:
                try:
                    revision_a = futures["revision_a"].result(timeout=180)
                    result.revision_a = revision_a
                    _notify("revision", {"by": "A", "text": revision_a})
                except Exception as e:
                    err = f"Phase 3: Claude revision failed: {type(e).__name__}: {e}"
                    logger.error(err)
                    result.errors.append(err)
                    _notify("error", err)

            if "revision_b" in futures:
                try:
                    revision_b = futures["revision_b"].result(timeout=180)
                    result.revision_b = revision_b
                    _notify("revision", {"by": "B", "text": revision_b})
                except Exception as e:
                    err = f"Phase 3: GPT revision failed: {type(e).__name__}: {e}"
                    logger.error(err)
                    result.errors.append(err)
                    _notify("error", err)

        result.phases_completed.append("phase3_revision")
        _notify("phase_end", "Phase 3 complete")

        # ── Phase 4: Final Judgment (Gemini) ───────────────────────
        _notify("phase_start", "Phase 4: Final Judgment (Gemini)")

        # Use revised versions if available, otherwise originals
        final_a = revision_a or rec_a
        final_b = revision_b or rec_b

        judge_message = build_judge_message(
            recommendation_a=rec_a,
            recommendation_b=rec_b,
            critique_of_a=critique_of_a or "(Critique not available)",
            critique_of_b=critique_of_b or "(Critique not available)",
            revision_a=revision_a or "(No revision — original proposal stands)",
            revision_b=revision_b or "(No revision — original proposal stands)",
            user_query=user_query,
        )

        try:
            judgment = self._call_openai_model(
                self.config.judge_model,
                JUDGE_SYSTEM_PROMPT,
                judge_message,
                self.config.judge_max_tokens,
            )
            result.judgment = judgment
            result.final_answer = judgment
            _notify("judgment", judgment)
            result.phases_completed.append("phase4_judgment")
        except Exception as e:
            err = f"Phase 4: Judge ({self.config.judge_model}) failed: {type(e).__name__}: {e}"
            logger.error(err)
            result.errors.append(err)
            _notify("error", err)
            # Fallback: use Claude's revised proposal (or original)
            result.final_answer = final_a

        _notify("phase_end", "Phase 4 complete")
        return result

    # ── Internal API Call Methods ──────────────────────────────────

    def _get_recommendation_a(self, user_query: str) -> str:
        """
        Get Claude's recommendation using the existing ReAct agent (with tools).
        This reuses the full agent.chat() pipeline.
        """
        # Reset conversation to avoid mixing with previous queries
        self.agent.reset()
        return self.agent.chat(user_query)

    def _get_recommendation_b(self, user_query: str) -> str:
        """Get GPT's recommendation via OpenAI-compatible API (text-only)."""
        message = build_recommender_b_message(user_query)
        return self._call_openai_model(
            self.config.recommender_b_model,
            RECOMMENDER_B_SYSTEM_PROMPT,
            message,
            self.config.recommender_b_max_tokens,
        )

    def _call_openai_model(
        self,
        model: str,
        system_prompt: str,
        user_message: str,
        max_tokens: int,
    ) -> str:
        """
        Unified OpenAI SDK call for GPT and Gemini models.

        All models are accessed through the same proxy with different model names.
        """
        response = self.openai_client.chat.completions.create(
            model=model,
            max_tokens=max_tokens,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content or ""

    def _call_claude_text_only(
        self,
        system_prompt: str,
        user_message: str,
        max_tokens: int,
    ) -> str:
        """
        Claude text-only call (no tools) for critique and revision phases.

        Uses the same Anthropic client from the agent but without tool schemas.
        """
        response = self.agent.client.messages.create(
            model=self.agent.config.model,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        text_parts = [b.text for b in response.content if b.type == "text"]
        return "\n".join(text_parts)
