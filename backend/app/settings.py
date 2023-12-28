from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    discord_token: str

    prefix: str = "!"

    db: str = "secretsanta.db"

    app_version: str = "0.0.1"