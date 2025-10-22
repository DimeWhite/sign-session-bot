from aiogram import Router, F
from aiogram.types import Message, Chat
from fluent.runtime import FluentLocalization
from keyboards import startSessionKeyboard, mainKeyboard, closeSessionKeyboard
from filters import L10nTextFilter
from services import openSession, closeSession
import asyncio
from aiogram.types import ReplyKeyboardRemove

router = Router()

@router.message(L10nTextFilter("start-session-button"))
async def startSessionHendler(
        message: Message,
        l10n: FluentLocalization,
):    
    await message.answer(
        l10n.format_value("start-session"),
        parse_mode=None,
        reply_markup=startSessionKeyboard(l10n),
    )
    
@router.message(F.location)
async def handleLocationHendler(message: Message, l10n: FluentLocalization,):
    lat, lon = message.location.latitude, message.location.longitude
    
    chat_data: Chat = message.chat
    
    await message.answer(
        l10n.format_value("send-geo"),
        parse_mode=None,
        reply_markup=closeSessionKeyboard(l10n),
    )
    asyncio.create_task(
        asyncio.to_thread(openSession, chat_data, [lat, lon])
    )

@router.message(L10nTextFilter("close-session-button"))
async def closeSessionHendler(
        message: Message,
        l10n: FluentLocalization,
):
    
    await message.answer(
        l10n.format_value("closing-session"),
        parse_mode=None,
        reply_markup=ReplyKeyboardRemove(selective=True),
    )
    
    index, duration = await asyncio.to_thread(closeSession, message.chat.id)
    answer = l10n.format_value("closed-session").format(number=index, duration=duration)
    
    await message.answer(
        answer,
        parse_mode=None,
        reply_markup=mainKeyboard(l10n),
    )

@router.message(L10nTextFilter("cancel-session-button"))
async def cancelSessionHendler(message: Message, l10n: FluentLocalization,):
    await message.answer(
        l10n.format_value("cancel-session"),
        parse_mode=None,
        reply_markup=mainKeyboard(l10n),
    )