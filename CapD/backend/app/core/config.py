from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_URL: str
    OPENAI_API_KEY: str
    QDRANT_HOST: str

    class Config:
        env_file = ".env"

settings = Settings()
