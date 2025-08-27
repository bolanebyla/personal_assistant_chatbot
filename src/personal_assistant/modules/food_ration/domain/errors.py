from commons.app_errors import AppError


class FoodRationDayAlreadyAddedToFoodRation(AppError):
    code = "food_ration.food_ration_day_already_added_to_food_ration"
    message_template = (
        "День рациона питания с id '{food_ration_day_id}' "
        "уже добавлен в рацион питания с id '{food_ration_id}'"
    )
