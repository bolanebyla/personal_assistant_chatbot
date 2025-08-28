from calendar import Day
from datetime import datetime

import pytest

from personal_assistant.modules.food_ration.domain import (
    FoodRation,
    FoodRationCreatedEvent,
    FoodRationDay,
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


def test__create_food_ration__create_event(frozen_datetime: datetime) -> None:
    food_ration = FoodRation(
        id="test_id",
        created_at=frozen_datetime,
        updated_at=frozen_datetime,
        user_id="test_user_id",
    )

    assert len(food_ration.domain_events) == 1
    assert isinstance(food_ration.domain_events[0], FoodRationCreatedEvent)

    event: FoodRationCreatedEvent = food_ration.domain_events[0]
    assert event.food_ration_id == food_ration.id


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
