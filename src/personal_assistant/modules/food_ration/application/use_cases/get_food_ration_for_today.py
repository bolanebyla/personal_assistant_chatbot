from datetime import UTC, datetime

from commons.entities import EntityId
from personal_assistant.modules.food_ration.application.dtos import DateFoodRationDayDto
from personal_assistant.modules.food_ration.application.interfaces import FoodRationDayReadRepo


class GetFoodRationForTodayUseCase:
    def __init__(self, food_ration_day_read_repo: FoodRationDayReadRepo):
        self._food_ration_day_read_repo = food_ration_day_read_repo

    def execute(self, user_id: EntityId) -> DateFoodRationDayDto | None:
        # TODO: реализовать логику поиска рациона питания на сегодня

        now = datetime.now(UTC)  # TODO: использовать часовой пояс пользователя

        user_today_food_ration = (
            self._food_ration_day_read_repo.get_food_ration_day_for_date_and_user(
                user_id=user_id,
                date=now,
            )
        )

        return user_today_food_ration
