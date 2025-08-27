from calendar import Day

import pytest
from freezegun import freeze_time

from personal_assistant.modules.food_ration.application.use_cases import (
    GetFoodRationForTodayUseCase,
    TodayFoodRationResultDto,
)


@pytest.fixture(scope="function")
def use_case() -> GetFoodRationForTodayUseCase:
    return GetFoodRationForTodayUseCase()


@freeze_time("2025-08-24")  # sunday
def test__get_food_ration_for_today(
    use_case: GetFoodRationForTodayUseCase,
) -> None:
    result = use_case.execute()

    assert isinstance(result, TodayFoodRationResultDto)
    assert result.week_day == Day.SUNDAY
