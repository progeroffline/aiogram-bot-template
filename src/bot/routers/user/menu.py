from aiogram import Router
from aiogram.types import CallbackQuery, InaccessibleMessage, Message
from aiogram_i18n import I18nContext


router = Router(name="menu")


async def user_welcome_message(
    message: Message | InaccessibleMessage | CallbackQuery,
    i18n: I18nContext,
):
    await message.answer(i18n.get("welcome_message"))
