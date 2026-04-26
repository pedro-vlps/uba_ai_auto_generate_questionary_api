"""Application settings and configuration management using environment variables."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    OPENAI_API_KEY: str
    FERNET_KEY: str
    JWT_SECRET_KEY: str
    ALGORITHM: str

    @property
    def database_url(self):
        """Build the database URL from individual components."""
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        """Configuration for loading environment variables from a .env file."""
        env_file = ".env"

settings = Settings() # type: ignore[call-arg]
