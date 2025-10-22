from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from fluent.runtime import FluentLocalization
from keyboards import mainKeyboard

router = Router()


@router.message(CommandStart())
async def cmd_start(
        message: Message,
        l10n: FluentLocalization,
):
    await message.answer(
        l10n.format_value("cmd-start"),
        parse_mode=None,
        reply_markup=mainKeyboard(l10n)
    )