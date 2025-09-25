from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    # database settings
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    # jwt settings
    JWT_ALGORITHM: str
    JWT_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = Path(__file__).resolve().parent.parent / ".env"  # backend/.env
        extra = "ignore"

settings = Settings()