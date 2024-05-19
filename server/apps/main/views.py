from datetime import date
from logging import getLogger

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import now

from . import crud
from . import time_utils
from .enums import CurrencyCode

logger = getLogger('django')


def per_day_spending_view(request: HttpRequest) -> HttpResponse:
    """Render a page with per-day spending data for all clients."""
    first_day, last_day = time_utils.get_month_range(
        now().date(),
        start_day=crud.get_budgeting_config().budgeting_start_day,
    )
    default_date_spending = {
        specific_date: 0
        for specific_date in time_utils.iterate_over_daterange(
            first_day,
            last_day,
        )
    }
    limit_remainders = crud.list_daily_cumulative_limit_remainders(
        currency=CurrencyCode.UAH,
        inclusive_date_range=(first_day, last_day),
    )
    spending_table: dict[str, dict[date, int]] = {
        client.name: default_date_spending | crud.list_daily_spending_for(
            client=client,
            currency=CurrencyCode.UAH,
            inclusive_date_range=(first_day, last_day),
        )
        for client in crud.list_clients()
    }

    logger.info(spending_table)
    logger.info(limit_remainders)
    return render(
        request, 'main/per_day_spending.html', {
            'all_clients_spending': spending_table,
            'currency': CurrencyCode.UAH,
            'from_date': first_day,
            'to_date': last_day,
            'unique_dates': sorted(
                default_date_spending.keys(),
                reverse=True,
            ),
            'limit_remainders': limit_remainders,
        },
    )
