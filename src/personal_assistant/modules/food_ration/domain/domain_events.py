from dataclasses import dataclass

from commons.entities import EntityId
from commons.events import BaseDomainEvent


@dataclass(frozen=True)
class FoodRationCreatedEvent(BaseDomainEvent):
    food_ration_id: EntityId


@dataclass(frozen=True)
class FoodRationDayCreatedEvent(BaseDomainEvent):
    food_ration_day_id: EntityId
