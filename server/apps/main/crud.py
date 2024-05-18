from datetime import date

from django.db.models import F as FieldRefResolver  # noqa: N811
from django.db.models import Sum

from .enums import CurrencyCode
from server.apps.main import models


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
    if of_interest_only:
        mcc_codes = models.MerchantCategoryCode.objects.filter(
            of_interest=True,
        ).values_list('code', flat=True)
        filtered_queryset = filtered_queryset.filter(mcc__in=mcc_codes)
    grouped_queryset = filtered_queryset.values(
        day=FieldRefResolver('time__date'),
    ).annotate(
        total_spending=Sum('amount'),
    ).order_by('day')
    return {
        entry['day']: abs(entry['total_spending'])
        for entry in grouped_queryset
    }
