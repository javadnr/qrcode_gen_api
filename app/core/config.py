from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "QR Code API"
    PROJECT_VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"     # ← load from .env automatically
        case_sensitive = True

settings = Settings()
