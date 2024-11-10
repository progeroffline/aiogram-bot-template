from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_i18n import I18nContext
from bot.routers.user.menu import user_welcome_message
from bot.repositories.user import UserRepository

router = Router(name="start")


@router.message(CommandStart())
async def start(
    message: Message,
    user_repository: UserRepository,
    i18n: I18nContext,
):
    if message.from_user is None:
        return

    if not await user_repository.exists(message.from_user.id):
        await user_repository.create(
            id=message.from_user.id,
            name=message.from_user.full_name,
            username=message.from_user.username,
        )

    return await user_welcome_message(message, i18n)
