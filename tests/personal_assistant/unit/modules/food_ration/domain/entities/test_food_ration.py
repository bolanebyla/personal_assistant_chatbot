from calendar import Day
from datetime import datetime

import pytest

from personal_assistant.modules.food_ration.domain.entities.food_ration import FoodRation
from personal_assistant.modules.food_ration.domain.entities.food_ration_day import FoodRationDay
from personal_assistant.modules.food_ration.domain.errors import (
    FoodRationDayAlreadyAddedToFoodRation,
)


@pytest.fixture(scope="function")
def food_ration(frozen_datetime: datetime) -> FoodRation:
    return FoodRation(
        id="test_id",
        created_at=frozen_datetime,
        updated_at=frozen_datetime,
        user_id="test_user_id",
    )


@pytest.fixture(scope="function")
def first_food_ration_day(frozen_datetime: datetime) -> FoodRationDay:
    return FoodRationDay(
        id="test_id",
        created_at=frozen_datetime,
        updated_at=frozen_datetime,
        weeks_interval=2,
        week_day=Day.MONDAY,
    )


def test__food_ration_add_food_ration_day(
    food_ration: FoodRation, first_food_ration_day: FoodRationDay
) -> None:
    food_ration.food_ration_days = []

    food_ration.add_food_ration_day(food_ration_day=first_food_ration_day)

    assert len(food_ration.food_ration_days) == 1
    assert food_ration.food_ration_days[0] == first_food_ration_day


def test__food_ration_add_food_ration_day__raise_food_ration_day_already_added(
    food_ration: FoodRation, first_food_ration_day: FoodRationDay
) -> None:
    food_ration.food_ration_days = [first_food_ration_day]

    with pytest.raises(FoodRationDayAlreadyAddedToFoodRation):
        food_ration.add_food_ration_day(food_ration_day=first_food_ration_day)
