from datetime import date
from logging import getLogger

from django.db import connection
from django.db.models import Sum
from django.db.models.functions import TruncDate

from .enums import CurrencyCode
from server.apps.main import models

logger = getLogger('django.server')


def list_clients(
    skip: int = 0,
    limit: int = 3,
) -> list[models.ClientInfo]:
    """List clients with pagination."""
    return list(models.ClientInfo.objects.all()[skip:skip + limit])


def get_budgeting_config() -> models.BudgetingConfig:
    """Get or create a budgeting config."""
    return models.BudgetingConfig.load()


def list_daily_spending_for(
    *,
    client: models.ClientInfo,
    currency: CurrencyCode,
    inclusive_date_range: tuple[date, date],
) -> dict[date, int]:
    """Spending aggregated by day for a specific client in absolute values."""
    mcc_codes = models.MerchantCategoryCode.objects.filter(
        of_interest=True,
    ).values_list('code', flat=True)
    filtered_queryset = models.StatementItem.objects.filter(
        account__client=client,
        currency_code=currency,
        time__date__range=inclusive_date_range,
        mcc__in=mcc_codes,
    )
    grouped_queryset = (
        filtered_queryset
        .annotate(day=TruncDate('time'))
        .values('day')
        .annotate(total_spending=Sum('operation_amount'))
        .order_by('day')
    )
    return {
        entry['day']: abs(entry['total_spending'])
        for entry in grouped_queryset
    }


def list_daily_cumulative_limit_remainders(
    *,
    currency: CurrencyCode,
    inclusive_date_range: tuple[date, date],
) -> dict[date, int]:
    """Calculate daily cumulative allowance remainers with daily overflows."""
    start_date, end_date = inclusive_date_range
    with connection.cursor() as cursor:
        cursor.execute(  # noqa: WPS462
            """
            WITH RECURSIVE
            DateRange(day) AS (
                SELECT %s
                UNION ALL
                SELECT date(day, '+1 day') FROM DateRange WHERE day <= %s
            ),
            MCCFilter AS (
                SELECT code FROM main.main_merchantcategorycode WHERE of_interest = 1
            ),
            DailyAllowance AS (
                SELECT daily_allowance FROM single_budgeting_config LIMIT 1  -- Assuming only one row exists
            ),
            DailySpending AS (
                SELECT
                    DATE(time) AS day,
                    SUM(operation_amount) AS total_spending
                FROM
                    statement_items
                WHERE
                    currency_code = %s AND
                    mcc IN (SELECT code FROM MCCFilter) AND
                    DATE(time) BETWEEN %s AND %s
                GROUP BY DATE(time)
            ),
            CumulativeResults AS (
                SELECT
                    dr.day,
                    COALESCE(SUM(ds.total_spending) OVER (ORDER BY dr.day), 0) AS cumulative_spending,
                    (SELECT daily_allowance FROM DailyAllowance) * (SELECT COUNT(*) FROM DateRange WHERE day <= dr.day) AS cumulative_allowance
                FROM
                    DateRange dr
                LEFT JOIN
                    DailySpending ds ON dr.day = ds.day
            )
            SELECT
                day,
                cumulative_allowance + cumulative_spending AS remaining_limit
            FROM
                CumulativeResults
            """,
            [
                start_date,
                end_date,
                currency.value,
                start_date,
                end_date,
            ],
        )
        return {
            date.fromisoformat(strdate): int(strremainder)
            for strdate, strremainder in cursor.fetchall()
        }
