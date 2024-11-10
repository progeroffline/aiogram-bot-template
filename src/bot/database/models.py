from sqlalchemy import Boolean, Column, BigInteger, String
from sqlalchemy.orm import Mapped
from bot.database.abstracts import ModelPrettyPrint


class User(ModelPrettyPrint):
    __tablename__ = "users"

    id: Mapped[int] = Column(
        BigInteger,
        primary_key=True,
        unique=True,
        autoincrement=False,
    )  # type: ignore
    name = Column(String, default="")
    username = Column(String, default="")
    is_admin = Column(Boolean, default=False)
