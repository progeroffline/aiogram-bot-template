from aiogram import Router
from bot.filters.admin import IsAdminFilter
from .menu import router as menu_router

router = Router(name="admin")
router.include_router(menu_router)

router.message.filter(IsAdminFilter())
router.callback_query.filter(IsAdminFilter())
