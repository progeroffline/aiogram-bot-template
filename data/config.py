# -*- coding: utf-8 -*-

from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

DB_HOST = env.str("DB_HOST")
DB_NAME = env.str("DB_NAME")
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")