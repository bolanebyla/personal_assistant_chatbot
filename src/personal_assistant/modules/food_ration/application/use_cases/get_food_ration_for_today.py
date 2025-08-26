from calendar import Day
from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(frozen=True)
class TodayFoodRationResultDto:
    week_day: Day


class GetFoodRationForTodayUseCase:
    def execute(self) -> TodayFoodRationResultDto | None:
        # TODO: реализовать логику поиска рациона питания на сегодня

        now = datetime.now(UTC)  # TODO: использовать часовой пояс пользователя
        return TodayFoodRationResultDto(week_day=Day(now.weekday()))
