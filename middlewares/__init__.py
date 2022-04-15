# -*- coding: utf-8 -*-

from loader import dp
from .logger_middleware import UpdateLoggerMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(UpdateLoggerMiddleware())