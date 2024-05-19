from collections.abc import Iterable
from datetime import date

from dateutil.relativedelta import relativedelta
from django.utils.timezone import make_aware
from django.utils.timezone import now
from django.utils.timezone import utc


def get_month_range(
    months_date: date,
    *,
    stop_today: bool = True,
) -> tuple[date, date]:
    """Get the start and end date of a month."""
    start = months_date.replace(day=1)
    today = date.today()
    end = start + relativedelta(months=1) - relativedelta(days=1)
    if end > today and stop_today:
        end = today
    return start, end


def iterate_over_daterange(start_date: date, end_date: date) -> Iterable[date]:
    """Iterate over a date range."""
    delta_stream = range((end_date - start_date).days + 1)
    return (
        start_date + relativedelta(days=delta)
        for delta in delta_stream
    )


def get_current_month_range() -> tuple[date, date]:
    """Get the start and end date of the current month."""
    return get_month_range(now().date())
