from collections.abc import Iterable
from datetime import date
from datetime import datetime
from datetime import time
from typing import Any

from dateutil.relativedelta import relativedelta
from django.utils.timezone import make_aware
from django.utils.timezone import now
from django.utils.timezone import utc


def get_month_range(months_date: date) -> tuple[date, date]:
    """Get the start and end date of a month."""
    start = months_date.replace(day=1)
    end = start + relativedelta(months=1) - relativedelta(days=1)
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


def to_aware_day_start(specific_date: date, tz: Any = utc) -> datetime:
    """Convert a date into a tz-aware datetime at the start of the day."""
    naive_datetime = datetime.combine(specific_date, time.min)
    aware_datetime = make_aware(naive_datetime, tz)
    return aware_datetime


def to_aware_day_end(specific_date: date, tz: Any = utc) -> datetime:
    """Convert a date into a tz-aware datetime at the end of the day."""
    naive_datetime = datetime.combine(specific_date, time.max)
    aware_datetime = make_aware(naive_datetime, tz)
    return aware_datetime
