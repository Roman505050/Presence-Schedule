from enum import StrEnum, auto, IntEnum

class Role(StrEnum):
    ADMIN = auto()
    MONITOR = auto()
    STUDENT = auto()

class Week(StrEnum):
    UPPER = auto()
    LOWER = auto()

class Day(IntEnum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()