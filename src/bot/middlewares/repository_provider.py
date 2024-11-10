from typing import Callable, Any, Awaitable, Type

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from bot.repositories.abstracts import BaseRepository


class RepositoryProviderMiddleware(BaseMiddleware):
    def __init__(self, repos: dict[str, Type[BaseRepository]]):
        self._repos = repos

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        session = data["session"]
        for repo in self._repos.keys():
            data[repo] = (self._repos[repo])(session)
        return await handler(event, data)
