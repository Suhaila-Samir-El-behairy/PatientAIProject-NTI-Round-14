"""Centralized settings, loaded from .env."""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    google_api_key: str
    llm_model: str = "gemini-2.0-flash-exp"
    llm_temperature: float = 0.0
    chroma_persist_dir: str = "./.chroma"
    kb_collection: str = "clinical_protocols"
    log_level: str = "INFO"
    app_lang_default: str = "ar-EG"
    pilot_hospital_name: str = "Pilot Hospital"
    emergency_sla_seconds: int = 30

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()