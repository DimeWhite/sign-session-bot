from uttils import Sheet
from aiogram.types import Chat
from typing import Tuple

def openSession(chat_data: Chat, geo: list[float]):
    sheet = Sheet()
    sheet.startSession(chat_data.id, chat_data.username or  "", chat_data.full_name, "gtybc")

def closeSession(user_id: int) -> Tuple[int, str]:
    sheet = Sheet()
    return sheet.closeSession(user_id)
