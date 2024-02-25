from sqlalchemy import (
    Integer,
    Column,
    Table,
    ForeignKey,
    UniqueConstraint
)
from .base import Base

students_groups_association_table = Table(
    "students_groups_association",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("students_id", ForeignKey("Students.id")),
    Column("groups_id", ForeignKey("Groups.id")),
    UniqueConstraint("students_id", "groups_id", name="unique_student_group"),
)
