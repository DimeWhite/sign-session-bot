from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from fluent.runtime import FluentLocalization

def mainKeyboard(l10n: FluentLocalization,) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=l10n.format_value("start-session-button"), callback_data="start-session")],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
        )