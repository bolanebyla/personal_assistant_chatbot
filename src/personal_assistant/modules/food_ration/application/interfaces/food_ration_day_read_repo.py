from datetime import datetime
from typing import Protocol, runtime_checkable

from commons.entities import EntityId
from personal_assistant.modules.food_ration.application.dtos import DateFoodRationDayDto


@runtime_checkable
class FoodRationDayReadRepo(Protocol):
    def get_food_ration_day_for_date_and_user(
        self, user_id: EntityId, date: datetime
    ) -> DateFoodRationDayDto:
        """Получает рацион на день для пользователя в определенную дату"""
        ...
