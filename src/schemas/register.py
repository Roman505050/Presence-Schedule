from pydantic import BaseModel
import datetime

class RegisterCreateSchema(BaseModel):
    student_id: int
    schedule_id: int
    date: datetime.date


class RegisterSchema(RegisterCreateSchema):
    id: int
    presence: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime