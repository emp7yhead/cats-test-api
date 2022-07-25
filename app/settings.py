from pydantic import BaseSettings


class Settings(BaseSettings):
    """Config app."""

    APP_NAME: str = 'CatsAPI'
    API_VERSION: str = '/v1'


settings = Settings()
