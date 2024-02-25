from pydantic import BaseModel
import datetime


class StudentsSchema(BaseModel):
    id: int
    last_name: str
    first_name: str
    patronymic_name: str
    photo_id: str
    telegram_id: int
    username: str
    role: str
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime

class GroupSchema(BaseModel):
    students: list[StudentsSchema]

class ScheduleSchema(BaseModel):
    id: int
    day: int
    week: int
    couple: int
    lesson: str
    teacher: str
    classroom: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    group: GroupSchema

    class Config:
        from_attributes = True