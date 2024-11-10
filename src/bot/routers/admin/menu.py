from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram_i18n import I18nContext
from bot.keyboards.admin import inline_keyboards
from bot.keyboards.admin.callback_types import AdminMenu
from bot.keyboards.admin.callback_values import AdminMenuActions


router = Router(name="menu")


@router.message(Command("admin"))
async def admin_menu(message: Message, i18n: I18nContext):
    await message.answer(
        text=i18n.get("admin_menu"),
        reply_markup=inline_keyboards.back_to_admin_menu(),
    )


@router.callback_query(
    AdminMenu.filter(F.action == AdminMenuActions.BACK_TO_ADMIN_MENU)
)
async def back_to_admin_menu(call: CallbackQuery, i18n: I18nContext):
    if call.message is None:
        return

    await call.message.answer(
        text=i18n.get("admin_menu"),
        reply_markup=inline_keyboards.back_to_admin_menu(),
    )
