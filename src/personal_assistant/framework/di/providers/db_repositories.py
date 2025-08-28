from dishka import Provider, Scope, provide

from personal_assistant.infrastructure.database.repositories import FoodRationDayReadRepoImpl
from personal_assistant.modules.food_ration.application.interfaces import FoodRationDayReadRepo


class DBRepositoriesProvider(Provider):
    scope = Scope.REQUEST

    food_ration_day_read_repo = provide(
        FoodRationDayReadRepoImpl,
        provides=FoodRationDayReadRepo,
    )
