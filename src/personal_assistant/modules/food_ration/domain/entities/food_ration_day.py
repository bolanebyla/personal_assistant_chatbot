from calendar import Day
from dataclasses import dataclass, field

from commons.entities import BaseEntity
from personal_assistant.modules.food_ration.domain.domain_events import FoodRationDayCreatedEvent


@dataclass(kw_only=True)
class FoodRationDay(BaseEntity):
    """День рациона питания"""

    week_day: Day
    weeks_interval: int

    dishes: list[str] = field(default_factory=list)  # TODO: сделать отдельными объектами

    def __post_init__(self) -> None:
        created_event = FoodRationDayCreatedEvent(food_ration_day_id=self.id)
        self._add_domain_event(created_event)
