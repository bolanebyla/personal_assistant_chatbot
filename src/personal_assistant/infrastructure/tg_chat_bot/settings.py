from pydantic_settings import BaseSettings


class TgBotSettings(BaseSettings):
    TOKEN: str

    class Config:
        env_prefix = "TG_BOT_"
