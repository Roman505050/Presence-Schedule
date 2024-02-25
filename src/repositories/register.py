from src.database.models import Register
from src.utils.repository import SQLAlchemyRepository

class RegisterRepository(SQLAlchemyRepository):
    model = Register