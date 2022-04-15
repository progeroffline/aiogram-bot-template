# -*- coding: utf-8 -*-

from .models import db
from data.config import DB_NAME, DB_HOST, DB_USER, DB_PASS


async def create_db(drop_all):
    await db.set_bind(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")

    if drop_all:
        await db.gino.drop_all()
        await db.gino.create_all()