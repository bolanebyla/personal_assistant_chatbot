from datetime import datetime

import pytest
from aiogram.types import Chat, Message, User
from pytest_mock import MockerFixture

from personal_assistant.infrastructure.tg_bot.handlers.food_ration import (
    today_food_ration_handler,
)
from personal_assistant.modules.food_ration.application.use_cases import (
    GetFoodRationForTodayUseCase,
)


@pytest.mark.asyncio
async def test_today_food_ration_handler__formated_food_ration(
    mocker: MockerFixture,
):
    mock_answer = mocker.AsyncMock()
    mocker.patch.object(Message, "answer", mock_answer)

    expected_message_text = "test_formated_food_ration_text"

    mocker.patch(
        target="personal_assistant.infrastructure.tg_bot.handlers.food_ration.format_today_food_ration_result_dto_to_str",
        return_value=expected_message_text,
    )

    message = Message(
        message_id=1,
        date=datetime(day=25, month=8, year=2025),
        chat=Chat(id=123, type="private"),
    )

    await today_food_ration_handler(message)

    mock_answer.assert_awaited_once_with(expected_message_text)


@pytest.mark.asyncio
async def test_today_food_ration_handler__empty(mocker: MockerFixture):
    mock_answer = mocker.AsyncMock()
    mocker.patch.object(Message, "answer", mock_answer)

    mock_use_case = mocker.Mock(spec=GetFoodRationForTodayUseCase)
    mock_use_case.execute.return_value = None

    mocker.patch(
        target="personal_assistant.infrastructure.tg_bot.handlers.food_ration.GetFoodRationForTodayUseCase",
        return_value=mock_use_case,
    )

    message = Message(
        message_id=1,
        date=datetime(day=25, month=8, year=2025),
        chat=Chat(id=123, type="private"),
    )

    await today_food_ration_handler(message)

    mock_answer.assert_awaited_once_with("Рацион на день ещё не сформирован 🙈")
