from datetime import date

from dateutil.relativedelta import relativedelta


def get_month_range(months_date: date) -> tuple[date, date]:
    """Get the start and end date of a month."""
    start = months_date.replace(day=1)
    end = start + relativedelta(months=1) - relativedelta(days=1)
    return start, end
