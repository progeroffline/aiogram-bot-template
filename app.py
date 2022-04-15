# -*- coding: utf-8 -*-

from loader import dp
from database import create_db
from aiogram import executor, Dispatcher


async def on_startup(dp: Dispatcher):
    import middlewares, handlers
    await create_db()


if __name__ == "__main__":
    executor.start_polling(dp=dp, on_startup=on_startup)