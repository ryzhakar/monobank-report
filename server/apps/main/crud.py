from datetime import date
from logging import getLogger

from django.db.models import Sum
from django.db.models.functions import TruncDate

from .enums import CurrencyCode
from server.apps.main import models

logger = getLogger('django.server')


def list_daily_spending_for(
    *,
    client: models.ClientInfo,
    currency: CurrencyCode,
    inclusive_date_range: tuple[date, date],
    of_interest_only: bool = False,
) -> dict[date, int]:
    """Spending aggregated by day for a specific client in absolute values."""
    filtered_queryset = models.StatementItem.objects.filter(
        account__client=client,
        currency_code=currency,
        time__date__range=inclusive_date_range,
    )
    logger.info('Filtered queryset: %s', filtered_queryset)
    if of_interest_only:
        mcc_codes = models.MerchantCategoryCode.objects.filter(
            of_interest=True,
        ).values_list('code', flat=True)
        filtered_queryset = filtered_queryset.filter(mcc__in=mcc_codes)
    grouped_queryset = (
        filtered_queryset
        .annotate(day=TruncDate('time'))
        .values('day')
        .annotate(total_spending=Sum('amount'))
        .order_by('day')
    )
    logger.info('Grouped queryset: %s', grouped_queryset)
    return {
        entry['day']: abs(entry['total_spending'])
        for entry in grouped_queryset
    }


def list_clients(
    skip: int = 0,
    limit: int = 3,
) -> list[models.ClientInfo]:
    """List clients with pagination."""
    return list(models.ClientInfo.objects.all()[skip:skip + limit])
