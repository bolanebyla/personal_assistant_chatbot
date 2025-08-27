from calendar import Day
from dataclasses import dataclass

from commons.entities import BaseEntity


@dataclass(kw_only=True)
class FoodRationDay(BaseEntity):
    """День рациона питания"""

    week_day: Day
    weeks_interval: int
