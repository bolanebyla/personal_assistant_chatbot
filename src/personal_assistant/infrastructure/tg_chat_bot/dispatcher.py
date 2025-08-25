from aiogram import Dispatcher

from personal_assistant.infrastructure.tg_chat_bot.handlers import (
    food_ration_router,
    start_router,
)

tg_bot_dispatcher = Dispatcher()

tg_bot_dispatcher.include_routers(
    start_router,
    food_ration_router,
)
