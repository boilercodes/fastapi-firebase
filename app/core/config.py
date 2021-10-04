from pydantic import BaseSettings


class Settings(BaseSettings):
    """The app settings."""

    PROJECT_NAME: str = "FastAPI"
    API_ENDPOINT: str = "/api/v1"

    API_PORT: int = 8080
    POSTGRES_URI: str = "postgresql://postgres:changeme@localhost:5432/postgres"

    class Config:
        """The Pydantic settings configuration."""

        env_file = ".env"


settings = Settings()
