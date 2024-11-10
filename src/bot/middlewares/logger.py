from collections.abc import Awaitable, Callable
from typing import Any
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from bot.dependencies import logger


class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        print(event)
        user_id = event.message.from_user.id if event.message else "Anonymous"  # type: ignore
        user_name = event.message.from_user.username if event.message else "No username"  # type: ignore
        chat_id = event.message.chat.id if event.message else "No chat"  # type: ignore
        message_text = event.message.text if event.message else "No message"  # type: ignore

        logger.info(
            f"User ID: {user_id}, Username: {user_name}, Chat ID: {chat_id}, Message: {message_text}"
        )

        return await handler(event, data)
