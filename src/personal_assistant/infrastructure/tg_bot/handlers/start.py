from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

from personal_assistant.infrastructure.tg_bot.keyboards.main_menu import (
    create_main_menu_keyboard,
)

start_router = Router(name="start")


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    main_menu_keyboard = create_main_menu_keyboard()

    await message.answer(
        f"Привет, {html.bold(message.from_user.first_name)}!\n"
        f"Я твой личный бот помощник 😁 Надеюсь на продуктивную работу 😉\n\n"
        f"Все мои функции доступны через меню ⌨️ \n\n"
        f"Если меню пропало, то его можно развернуть, "
        f"нажав на соответсвующую кнопку возле смайликов, "
        f"либо вызвать команду /start",
        reply_markup=main_menu_keyboard,
    )
