"""Shared LLM client (Gemini 2.0 Flash, free tier)."""
from functools import lru_cache
from langchain_google_genai import ChatGoogleGenerativeAI
from apps.agents.shared.config import settings

@lru_cache(maxsize=1)
def get_llm() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=settings.llm_model,
        temperature=settings.llm_temperature,
        google_api_key=settings.google_api_key,
    )

@lru_cache(maxsize=1)
def get_llm_json() -> ChatGoogleGenerativeAI:
    """LLM that returns strict JSON. Used for triage scoring."""
    return ChatGoogleGenerativeAI(
        model=settings.llm_model,
        temperature=0.0,
        google_api_key=settings.google_api_key,
    )