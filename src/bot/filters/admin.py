from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message, TelegramObject
from bot.config_reader import Settings
from bot.repositories.user import UserRepository

settings = Settings()  # type: ignore


class IsAdminFilter(BaseFilter):
    async def __call__(
        self,
        obj: TelegramObject,
        user_repository: UserRepository,
    ) -> bool:
        if isinstance(obj, Message):
            user_id = obj.from_user.id  # type: ignore
        elif isinstance(obj, CallbackQuery):
            user_id = obj.from_user.id
        else:
            return False

        if settings.super_admin_telegram_id == user_id:
            return True

        return await user_repository.is_admin(user_id)
