# -*- coding: utf-8 -*-

from data.config import BOT_TOKEN
from aiogram import types
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from logzero import logger, logfile


logfile("logs/bot_log.log", maxBytes=10_000_000, backupCount=20)

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)