from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    Numeric
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
from src.database.enums import Week, Day


class Schedule(Base):
    __tablename__ = "Schedule"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("Groups.id"), nullable=False)
    week: Mapped[Week] = mapped_column(nullable=False)
    day: Mapped[Day] = mapped_column(String(20), nullable=False)
    couple: Mapped[int] = mapped_column(Numeric(1), nullable=False)
    lesson: Mapped[str] = mapped_column(String(255), nullable=False)
    teacher: Mapped[str] = mapped_column(String(255), nullable=False)
    classroom: Mapped[str] = mapped_column(String(10), nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    group = relationship("Groups", back_populates="schedule")