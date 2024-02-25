__all__ = (
    'RegisterSchema',
    'RegisterCreateSchema',
    'ScheduleSchema',
    'GroupSchema',
    'StudentsSchema',
)

from .register import RegisterSchema, RegisterCreateSchema
from .schedule import ScheduleSchema, GroupSchema, StudentsSchema