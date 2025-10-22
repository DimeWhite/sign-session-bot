from uttils import Sheet
from aiogram.types import Chat
from typing import Tuple

def openSession(chat_data: Chat, geo: list[float]):
    Sheet().startSession(chat_data.id, chat_data.username or  "", chat_data.full_name, "gtybc")

def closeSession(user_id: int) -> Tuple[int, str]:
    return Sheet().closeSession(user_id)

def cancelSession(user_id: int):
    Sheet().cancelSession(user_id)