from pydantic_settings import BaseSettings
from pydantic import SecretStr
from pathlib import Path


class Settings(BaseSettings):
    bot_token: SecretStr

    db_driver: str = "postgresql+psycopg"
    db_host: str
    db_port: int = 5432
    db_user: str
    db_password: str
    db_name: str

    super_admin_telegram_id: int

    logger_logfile_path: Path = (
        Path(__file__).resolve().parent.joinpath("logs", "bot.log")
    )

    class Config:
        env_file = Path(__file__).resolve().parent.parent.parent.joinpath(".env")
        env_file_encoding = "utf-8"

    def get_postgres_dsn_url(self) -> str:
        return f"{self.db_driver}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()  # type: ignore
