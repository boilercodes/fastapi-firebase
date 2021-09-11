from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI"
    API_V1_STR: str = "/api/v1"

    API_PORT: int = 8080
    POSTGRES_URI: str = "postgresql://postgres:changeme@localhost:5432/postgres"

    class Config:
        env_file = ".env"


settings = Settings()
