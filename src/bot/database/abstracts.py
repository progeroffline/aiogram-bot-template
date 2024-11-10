from bot.database.base import Base


class ModelPrettyPrint(Base):
    __abstract__ = True

    def __repr__(self):
        attrs = [
            (column.name, getattr(self, column.name))
            for column in self.__table__.columns
        ]
        attrs_str = ", ".join(f"{name}={value!r}" for name, value in attrs)
        return f"<{self.__class__.__name__}({attrs_str})>"
