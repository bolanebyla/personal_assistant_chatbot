from datetime import datetime

import pytest
from aiogram.types import Chat, Message, User
from pytest_mock import MockerFixture

from personal_assistant.infrastructure.tg_bot.handlers.default import (
    default_handler,
)
from personal_assistant.infrastructure.tg_bot.keyboards.main_menu import (
    create_main_menu_keyboard,
)


@pytest.mark.asyncio
async def test_default_handler(mocker: MockerFixture):
    mock_answer = mocker.AsyncMock()
    mocker.patch.object(Message, "answer", mock_answer)

    # Создаём тестовое сообщение
    message = Message(
        message_id=1,
        date=datetime(day=25, month=8, year=2025),
        chat=Chat(id=123, type="private"),
        from_user=User(id=456, is_bot=False, first_name="Test"),
        text="Что-то непонятное",
    )

    await default_handler(message)

    mock_answer.assert_awaited_once_with(
        "Я вас не понял 😬\nВоспользуйтесь меню 😉",
        reply_markup=create_main_menu_keyboard(),
    )
