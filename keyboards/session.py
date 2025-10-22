from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from fluent.runtime import FluentLocalization

def startSessionKeyboard(l10n: FluentLocalization,) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=l10n.format_value("send-geo-button"), request_location=True)],
            [KeyboardButton(text=l10n.format_value("cancel-session-button"))],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
        )
    

def closeSessionKeyboard(l10n: FluentLocalization,) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=l10n.format_value("close-session-button"))],
            [KeyboardButton(text=l10n.format_value("cancel-recorded-session-button"))],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
        )
    