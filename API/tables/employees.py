from sqlalchemy import ForeignKey
from basic.table import BaseTable
from sqlalchemy.orm import Mapped, mapped_column, relationship

class EmployeePosition(BaseTable):
    __tablename__ = "employee_positions"

    name: Mapped[str]
    duties: Mapped[str | None]

    employees = relationship("Employee", back_populates="position")

class Employee(BaseTable):
    __tablename__ = "employees"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    position_id: Mapped[int] = mapped_column(ForeignKey("employee_positions.id"))

    user = relationship("UserTable", back_populates="employee")
    position = relationship("EmployeePosition", back_populates="employees")