from sqlalchemy import ForeignKey
from basic.table import BaseTable
from sqlalchemy.orm import Mapped, mapped_column, relationship

class NotificationTable(BaseTable):
    __tablename__ = "notifications"
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    message: Mapped[dict]

    user = relationship("UserTable", back_populates="notifications")