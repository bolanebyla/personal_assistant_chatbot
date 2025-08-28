from calendar import Day

from aiogram import F, Router
from aiogram.types import Message
from dishka import FromDishka

from personal_assistant.infrastructure.tg_bot.keyboards.main_menu import (
    TODAY_FOOD_RATION_MESSAGE_TEXT,
)
from personal_assistant.modules.food_ration.application.dtos import DateFoodRationDayDto
from personal_assistant.modules.food_ration.application.use_cases import (
    GetFoodRationForTodayUseCase,
)

food_ration_router = Router(name="food_ration")

WEEK_DAY_RU_MAPPING = {
    Day.MONDAY: "Понедельник",
    Day.TUESDAY: "Вторник",
    Day.WEDNESDAY: "Среда",
    Day.THURSDAY: "Четверг",
    Day.FRIDAY: "Пятница",
    Day.SATURDAY: "Суббота",
    Day.SUNDAY: "Воскресенье",
}


def format_today_food_ration_result_dto_to_str(
    today_food_ration_result_dto: DateFoodRationDayDto,
) -> str:
    week_day_ru = WEEK_DAY_RU_MAPPING.get(
        today_food_ration_result_dto.week_day,
        today_food_ration_result_dto.week_day.name,
    )

    dishes = ""
    for dish in today_food_ration_result_dto.dishes:
        dishes += f"- {dish}\n"
    # TODO: реализовать корректное форматирование
    return f"<b>{week_day_ru}</b>\n=======================\n{dishes}"


@food_ration_router.message(F.text == TODAY_FOOD_RATION_MESSAGE_TEXT)
async def today_food_ration_handler(
    message: Message,
    use_case: FromDishka[GetFoodRationForTodayUseCase],
) -> None:
    user_id = "1234"  # TODO: получать id пользователя

    today_food_ration_result_dto = use_case.execute(user_id=user_id)

    if today_food_ration_result_dto is None:
        await message.answer("Рацион на день ещё не сформирован 🙈")
    else:
        formated_today_food_ration = format_today_food_ration_result_dto_to_str(
            today_food_ration_result_dto=today_food_ration_result_dto
        )
        await message.answer(formated_today_food_ration)
