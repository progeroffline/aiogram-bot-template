import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from bot.config_reader import settings
from bot.middlewares.logger import LoggingMiddleware
from bot.routers import start, admin
from bot.ui_commands import set_ui_commands
from bot.dependencies import i18n_middleware, session_provider, repo_provider


async def main():
    bot = Bot(
        settings.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher()

    dp.update.middleware(LoggingMiddleware())
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    dp.message.middleware(session_provider)
    dp.message.middleware(repo_provider)

    dp.callback_query.middleware(session_provider)
    dp.callback_query.middleware(repo_provider)

    dp.include_router(start.router)
    dp.include_router(admin.router)

    i18n_middleware.setup(dispatcher=dp)

    await set_ui_commands(bot)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
