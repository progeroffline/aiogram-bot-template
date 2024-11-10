from aiogram_i18n import LazyProxy
from aiogram_i18n.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.keyboards.admin.callback_types import AdminMenu
from bot.keyboards.admin.callback_values import AdminMenuActions


def back_to_admin_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=LazyProxy("back_to_admin_menu"),
                    callback_data=AdminMenu(
                        action=AdminMenuActions.BACK_TO_ADMIN_MENU
                    ).pack(),
                )
            ],
        ]
    )
