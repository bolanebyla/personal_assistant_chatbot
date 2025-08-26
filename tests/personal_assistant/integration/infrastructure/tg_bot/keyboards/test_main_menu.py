from aiogram.types import ReplyKeyboardMarkup

from personal_assistant.infrastructure.tg_bot.keyboards.main_menu import (
    create_main_menu_keyboard,
)


def test_create_main_menu_keyboard() -> None:
    main_menu_keyboard = create_main_menu_keyboard()

    assert isinstance(main_menu_keyboard, ReplyKeyboardMarkup)
    assert main_menu_keyboard.resize_keyboard is True
    assert len(main_menu_keyboard.keyboard) == 1
    assert main_menu_keyboard.keyboard[0][0].text == "Рацион на день"
