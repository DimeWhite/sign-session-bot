from aiogram import Router

from . import main, session


def get_routers() -> list[Router]:
    return [
        main.router,
        session.router,
    ]