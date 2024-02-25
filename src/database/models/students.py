from sqlalchemy import (
    Integer,
    String,
    Boolean, 
    ForeignKey, 
    Numeric
)
from sqlalchemy.orm import (
    relationship, 
    Mapped, 
    mapped_column, 
    relationship
)
from src.database.enums import Role
from src.database.models.models import (
    created_at, 
    updated_at
)
from .base import Base
from .students_groups_association import (
    students_groups_association_table
)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .groups import Groups

class Students(Base):
    __tablename__ = "Students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    patronymic_name: Mapped[str] = mapped_column(String(255), nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    photo_id: Mapped[str] = mapped_column(String(255), nullable=False)
    telegram_id: Mapped[int] = mapped_column(Integer, nullable=False)
    role: Mapped[Role] = mapped_column(String(30), nullable=False, default=Role.STUDENT.value)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    groups: Mapped[list["Groups"]] = relationship(
        secondary=students_groups_association_table,
        back_populates="students"
    )