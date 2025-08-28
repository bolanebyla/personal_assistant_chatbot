from calendar import Day
from datetime import datetime

from personal_assistant.modules.food_ration.domain import FoodRationDay, FoodRationDayCreatedEvent


def test__create_food_ration_day__create_event(frozen_datetime: datetime) -> None:
    food_ration_day = FoodRationDay(
        id="test_id",
        created_at=frozen_datetime,
        updated_at=frozen_datetime,
        weeks_interval=2,
        week_day=Day.MONDAY,
    )
    assert len(food_ration_day.domain_events) == 1
    assert isinstance(food_ration_day.domain_events[0], FoodRationDayCreatedEvent)

    event: FoodRationDayCreatedEvent = food_ration_day.domain_events[0]
    assert event.food_ration_day_id == food_ration_day.id
