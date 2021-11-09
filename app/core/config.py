from pydantic import BaseSettings, PostgresDsn


class API(BaseSettings):
    """The API settings."""

    name: str = "FastAPI"
    endpoint: str = "/api/v1"

    host: str = "0.0.0.0"
    port: int = 8080

    class Config:
        """The Pydantic settings configuration."""

        env_file = ".env"
        env_prefix = "API_"


class Global(BaseSettings):
    """The app settings."""

    api: API = API()
    pg_dns: PostgresDsn = "postgresql://postgres:changeme@localhost:5432/postgres"
    sqlite_dns: str = "sqlite:///db.sqlite3"

    debug: bool = False

    class Config:
        """The Pydantic settings configuration."""

        env_file = ".env"
        fields = {
            "pg_dns": {
                "env": "POSTGRES_URI"
            }
        }


settings = Global()
