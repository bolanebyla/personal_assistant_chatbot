from dishka import Provider, Scope, provide

from personal_assistant.modules.food_ration.application.use_cases import (
    GetFoodRationForTodayUseCase,
)


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    get_food_ration_for_today = provide(
        GetFoodRationForTodayUseCase,
    )
