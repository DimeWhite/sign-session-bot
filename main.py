import asyncio
from handlers import get_routers
from aiogram import Bot, Dispatcher
from fluent_loader import get_fluent_localization
from middlewares import L10nMiddleware
from config_reader import config

async def main():
    locale = get_fluent_localization()

    dp = Dispatcher()
    dp.message.outer_middleware(L10nMiddleware(locale))
    dp.message.middleware(L10nMiddleware(locale))

    dp.pre_checkout_query.outer_middleware(L10nMiddleware(locale))
    dp.callback_query.middleware(L10nMiddleware(locale))

    dp.include_routers(*get_routers())

    bot = Bot(config.bot_token.get_secret_value())
    await dp.start_polling(bot)

    
if __name__ == "__main__":
    asyncio.run(main())