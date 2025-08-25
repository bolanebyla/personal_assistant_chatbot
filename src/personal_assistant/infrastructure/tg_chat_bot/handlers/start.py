from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from personal_assistant.infrastructure.tg_chat_bot.handlers.food_ration import (
    TODAY_FOOD_RATION_MESSAGE_TEXT,
)

start_router = Router(name="start")


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    builder = ReplyKeyboardBuilder()
    builder.button(text=TODAY_FOOD_RATION_MESSAGE_TEXT)

    await message.answer(
        f"Hello, {html.bold(message.from_user.full_name)}!",
        reply_markup=builder.as_markup(),
    )
