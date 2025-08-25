from aiogram import Router
from aiogram.types import Message

from personal_assistant.infrastructure.tg_chat_bot.keyboards.main_menu import (
    create_main_menu_keyboard,
)

default_router = Router(name="default")


@default_router.message()
async def echo_handler(message: Message) -> None:
    main_menu_keyboard = create_main_menu_keyboard()

    await message.answer(
        "Я вас не понял 😬\nВоспользуйтесь меню 😉",
        reply_markup=main_menu_keyboard,
    )
