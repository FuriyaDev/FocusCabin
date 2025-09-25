from basic.table import BaseTable
from sqlalchemy.orm import Mapped

class UsersTable(BaseTable):
    __tablename__ = "users"
    
    username: Mapped[str]
    password: Mapped[str]
    telegram_chat_id: Mapped[int]
    first_name: Mapped[str]
    last_name: Mapped[str]
    phone_number: Mapped[str]
    passport_front: Mapped[str]
    passport_back: Mapped[str]
    is_block: Mapped[bool]
    is_verified: Mapped[bool]
    profile_image: Mapped[str]
