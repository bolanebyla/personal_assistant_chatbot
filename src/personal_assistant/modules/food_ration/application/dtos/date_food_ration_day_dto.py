from calendar import Day
from dataclasses import dataclass, field


@dataclass
class DateFoodRationDayDto:
    week_day: Day
    dishes: list[str] = field(default_factory=list)  # TODO: сделать отдельными объектами
