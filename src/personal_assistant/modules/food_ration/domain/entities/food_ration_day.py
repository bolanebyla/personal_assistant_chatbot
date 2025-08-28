from calendar import Day
from dataclasses import dataclass

from commons.entities import BaseEntity
from personal_assistant.modules.food_ration.domain.domain_events import FoodRationDayCreatedEvent


@dataclass(kw_only=True)
class FoodRationDay(BaseEntity):
    """День рациона питания"""

    week_day: Day
    weeks_interval: int

    def __post_init__(self) -> None:
        created_event = FoodRationDayCreatedEvent(food_ration_day_id=self.id)
        self._add_domain_event(created_event)
