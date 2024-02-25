from sqlalchemy import (
    Integer,
    String,
    Numeric,
    ForeignKey
)
from sqlalchemy.orm import (
    relationship, 
    Mapped, 
    mapped_column, 
)
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
    from .students import Students

class Groups(Base):
    __tablename__ = "Groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    course: Mapped[int] = mapped_column(Numeric(1), nullable=False)
    year: Mapped[int] = mapped_column(Numeric(4), nullable=False)
    monitor_id: Mapped[int] = mapped_column(ForeignKey("Students.id"), nullable=False)
    profession: Mapped[int] = mapped_column(Numeric(3), nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    schedule = relationship("Schedule", back_populates="group")
    students: Mapped[list["Students"]] = relationship(
        secondary=students_groups_association_table,
        back_populates="groups"
    )

