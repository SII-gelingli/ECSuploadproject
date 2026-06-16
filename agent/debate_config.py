"""
Configuration for the multi-model debate mechanism.

Defines DebateConfig with model names, token limits, and API settings.
All models share the same API key and base URL (via a unified proxy).
"""
import os
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DebateConfig:
    """Configuration for the debate-based multi-model collaboration."""

    enabled: bool = False

    # Recommender B model (GPT-5.4, text-only reasoning)
    recommender_b_model: str = "gpt-5.4"

    # Judge model (Gemini 3.1 Pro)
    judge_model: str = "gemini-3.1-pro-preview"

    # Token limits
    recommender_b_max_tokens: int = 4096
    critic_max_tokens: int = 3000
    revision_max_tokens: int = 4000
    judge_max_tokens: int = 4096

    # API configuration (shared proxy key and URL)
    api_key: Optional[str] = field(
        default_factory=lambda: os.environ.get("ANTHROPIC_API_KEY")
    )
    base_url: Optional[str] = field(
        default_factory=lambda: os.environ.get("ANTHROPIC_BASE_URL")
    )
