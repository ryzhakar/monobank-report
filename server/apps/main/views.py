from datetime import date

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import now

from .crud import list_clients
from .crud import list_daily_spending_for
from .enums import CurrencyCode
from .time_utils import get_month_range
from .time_utils import iterate_over_daterange


def per_day_spending_view(request: HttpRequest) -> HttpResponse:
    """Render a page with per-day spending data for all clients."""
    first_day, last_day = get_month_range(now().date())
    default_date_spending = {
        specific_date: 0
        for specific_date in iterate_over_daterange(first_day, last_day)
    }
    spending_table: dict[str, dict[date, int]] = {
        client.name: default_date_spending | list_daily_spending_for(
            client=client,
            currency=CurrencyCode.UAH,
            inclusive_date_range=(first_day, last_day),
            of_interest_only=False,
        )
        for client in list_clients()
    }

    return render(
        request, 'main/per_day_spending.html', {
            'all_clients_spending': spending_table,
            'currency': CurrencyCode.UAH,
            'from_date': first_day,
            'to_date': last_day,
        },
    )
