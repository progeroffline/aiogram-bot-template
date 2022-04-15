# -*- coding: utf-8 -*-

from loader import logger
from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


class UpdateLoggerMiddleware(BaseMiddleware):
    async def on_process_update(self, update: types.Update, data: dict):
        logger.info(update)