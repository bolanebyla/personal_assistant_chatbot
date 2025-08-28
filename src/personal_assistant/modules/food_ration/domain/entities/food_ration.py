from dataclasses import dataclass, field

from commons.entities import BaseAggregateRoot, EntityId
from personal_assistant.modules.food_ration.domain.domain_events import FoodRationCreatedEvent
from personal_assistant.modules.food_ration.domain.errors import (
    FoodRationDayAlreadyAddedToFoodRation,
)

from .food_ration_day import FoodRationDay


@dataclass(kw_only=True)
class FoodRation(BaseAggregateRoot):
    """Рацион питания"""

    user_id: EntityId
    food_ration_days: list[FoodRationDay] = field(default_factory=list)

    def __post_init__(self) -> None:
        created_event = FoodRationCreatedEvent(food_ration_id=self.id)
        self._add_domain_event(created_event)

    def add_food_ration_day(self, food_ration_day: FoodRationDay) -> None:
        if food_ration_day in self.food_ration_days:
            raise FoodRationDayAlreadyAddedToFoodRation(
                food_ration_day_id=food_ration_day.id,
                food_ration_id=self.id,
            )

        self.food_ration_days.append(food_ration_day)
