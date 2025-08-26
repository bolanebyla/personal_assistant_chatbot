from calendar import Day
from dataclasses import dataclass
from uuid import UUID


@dataclass(kw_only=True)
class FoodRationDay:
    """День рациона питания"""

    id: UUID
    week_day: Day
    weeks_interval: int
