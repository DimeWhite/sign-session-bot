from uttils import Sheet, geoLocate
from aiogram.types import Chat
from typing import Tuple

def openSession(chat_data: Chat, geo: list[float]):
    address = geoLocate(geo[0], geo[1])    
    username = chat_data.username or  ""
    Sheet().startSession(chat_data.id, username, chat_data.full_name, address)

def closeSession(user_id: int) -> Tuple[int, str]:
    return Sheet().closeSession(user_id)

def commentSession(user_id: int, comment: str):
    Sheet().commentSession(user_id, comment)

def cancelSession(user_id: int):
    Sheet().cancelSession(user_id)