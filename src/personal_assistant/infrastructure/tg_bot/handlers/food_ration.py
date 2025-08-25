from aiogram import F, Router
from aiogram.types import Message

from personal_assistant.infrastructure.tg_bot.keyboards.main_menu import (
    TODAY_FOOD_RATION_MESSAGE_TEXT,
)

food_ration_router = Router(name="food_ration")


@food_ration_router.message(F.text == TODAY_FOOD_RATION_MESSAGE_TEXT)
async def food_ration_handler(message: Message) -> None:
    await message.answer("Рацион на день ещё не сформирован 🙈")
