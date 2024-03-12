import datetime

from src.database.enums import Week


def get_week_type() -> Week:
    today = datetime.date().today()  # Поточна дата
    iso_week_number = today.isocalendar()[1]  # Отримати номер тижня за ISO стандартом
    first_day_of_month = today.replace(day=1)  # Перший день поточного місяця
    first_day_of_month_week_number = first_day_of_month.isocalendar()[1]  # Номер тижня першого дня місяця
    current_week_number = iso_week_number - first_day_of_month_week_number + 1
    
    if current_week_number % 2 == 0:
        return Week.UPPER  # Верхній тиждень
    else:
        return Week.LOWER  # Нижній тиждень