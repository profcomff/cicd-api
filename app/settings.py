from functools import lru_cache

from pydantic import AnyUrl, BaseSettings, PostgresDsn


class Settings(BaseSettings):
    """Application settings"""

    CORS_ALLOW_ORIGINS: list[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ['*']
    CORS_ALLOW_HEADERS: list[str] = ['*']

    AUTH_URL: AnyUrl = "https://auth.api.test.profcomff.com/"

    class Config:
        """Pydantic BaseSettings config"""

        case_sensitive = True
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
