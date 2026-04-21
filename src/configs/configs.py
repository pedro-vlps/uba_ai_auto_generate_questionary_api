from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    OPENAI_API_KEY: str
    FERNET_KEY: str

    @property
    def DATABASE_URL(self):
        """Build the database URL from individual components."""
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@db:5432/{self.POSTGRES_DB}"
        )

    class Config:
        """Configuration for loading environment variables from a .env file."""
        env_file = ".env"

settings = Settings() # type: ignore[call-arg]
