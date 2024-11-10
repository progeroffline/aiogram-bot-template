from aiogram.filters.callback_data import CallbackData

from bot.keyboards.admin.callback_values import AdminMenuActions


class AdminMenu(CallbackData, prefix="admin_menu"):
    action: AdminMenuActions
