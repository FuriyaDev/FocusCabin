from basic.table import BaseTable
from sqlalchemy.orm import Mapped, mapped_column

class UsersTable(BaseTable):
    __tablename__ = "users"
    
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    telegram_chat_id: Mapped[int | None]
    first_name: Mapped[str]
    last_name: Mapped[str]
    phone_number: Mapped[str | None] = mapped_column(unique=True)
    passport_front: Mapped[str | None]
    passport_back: Mapped[str | None]
    is_block: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)
    profile_image: Mapped[str | None] = mapped_column(nullable=True, default="default/profile_image.png")

