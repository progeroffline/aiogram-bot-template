from typing import Optional, Sequence

from sqlalchemy import select, update
from bot.database.models import User
from bot.repositories.abstracts import BaseRepository


class UserRepository(BaseRepository):
    async def create(
        self,
        id: int,
        name: Optional[str] = None,
        username: Optional[str] = None,
    ) -> User:
        user = User(id=id, name=name, username=username)
        self._session.add(user)
        await self._session.commit()
        return user

    async def get_user_by_id(self, user_id: int) -> User | None:
        query = select(User).filter_by(id=user_id)
        return await self._session.scalar(query)

    async def exists(
        self,
        id: Optional[int] = None,
        username: Optional[str] = None,
    ) -> bool:
        query = None

        if id:
            query = select(User.id).filter_by(id=id).limit(1)
        if username:
            query = select(User.id).filter_by(username=username).limit(1)

        if query is not None:
            return await self._session.scalar(query) is not None
        return False

    async def is_admin(self, id: int) -> bool:
        query = select(User.is_admin).where(User.id == id)
        result = await self._session.scalar(query)
        return bool(result)

    async def set_admin_by_username(self, username: str) -> None:
        query = (
            update(User)
            .where(User.username == username)
            .values(is_admin=True)
            .execution_options(synchronize_session="fetch")
        )
        await self._session.execute(query)
        await self._session.commit()

    async def unset_admin_by_username(self, username: str) -> None:
        query = (
            update(User)
            .where(User.username == username)
            .values(is_admin=False)
            .execution_options(synchronize_session="fetch")
        )
        await self._session.execute(query)
        await self._session.commit()

    async def get_admins(self) -> Sequence[User]:
        query = select(User).where(User.is_admin)
        result = await self._session.scalars(query)
        return result.all()
