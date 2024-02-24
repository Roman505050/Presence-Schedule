from src.database.models import Schedule
from src.utils.repository import SQLAlchemyRepository

class ScheduleRepository(SQLAlchemyRepository):
    model = Schedule