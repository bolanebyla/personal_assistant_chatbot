from calendar import Day
from datetime import datetime

from commons.entities import EntityId
from personal_assistant.modules.food_ration.application.dtos import DateFoodRationDayDto
from personal_assistant.modules.food_ration.application.interfaces import FoodRationDayReadRepo


class FoodRationDayReadRepoImpl(FoodRationDayReadRepo):
    def get_food_ration_day_for_date_and_user(
        self, user_id: EntityId, date: datetime
    ) -> DateFoodRationDayDto:
        """Получает рацион на день для пользователя в определенную дату"""
        return DateFoodRationDayDto(
            week_day=Day(date.weekday()),
            dishes=["Каша", "Яйца", "Кофе"],
        )
