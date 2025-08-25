from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from .settings import TgBotSettings

# TODO: создавать бота в DI контейнере
tg_bot_settings = TgBotSettings()

tg_bot = Bot(
    token=tg_bot_settings.TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
