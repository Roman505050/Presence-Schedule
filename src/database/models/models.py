from sqlalchemy import (
    DateTime,
)
from sqlalchemy.orm import (
    mapped_column
)
from sqlalchemy.sql import func
from typing import Annotated
import datetime
from src.config import settings

created_at = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True), default=func.timezone(settings.TIMEZONE, func.now()))]
updated_at = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True), 
        default=func.timezone(settings.TIMEZONE, func.now()),
        onupdate=func.timezone(settings.TIMEZONE, func.now())
    )]