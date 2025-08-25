from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TODAY_FOOD_RATION_MESSAGE_TEXT = "Рацион на день"


def create_main_menu_keyboard() -> ReplyKeyboardMarkup:
    main_menu_keyboard_builder = ReplyKeyboardBuilder()
    main_menu_keyboard_builder.button(text=TODAY_FOOD_RATION_MESSAGE_TEXT)
    return main_menu_keyboard_builder.as_markup(resize_keyboard=True)
