# -*- coding: utf-8 -*-

from aiogram import Dispatcher, executor

from database import create_db
from loader import dp


async def on_startup(dp: Dispatcher):
    import handlers
    import middlewares
    await create_db()


if __name__ == "__main__":
    executor.start_polling(on_startup=on_startup)
