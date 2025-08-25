from aiogram import F, Router
from aiogram.types import Message

food_ration_router = Router(name="food_ration")

TODAY_FOOD_RATION_MESSAGE_TEXT = "Меню на день"


@food_ration_router.message(F.text == TODAY_FOOD_RATION_MESSAGE_TEXT)
async def echo_handler(message: Message) -> None:
    await message.answer("Маню на день ещё не сформировано 🙈")
