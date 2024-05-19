from collections.abc import Hashable
from typing import Any

from django import template

register = template.Library()


@register.filter
def get_item(dictionary: dict[Hashable, Any], some_key: Hashable) -> Any:
    """Dictionary lookup by key."""
    return dictionary.get(some_key)


@register.filter
def humanize_monetary(monetary_integer: int) -> str:
    """Represent as UAH without fractional part."""
    return '{full_units} UAH'.format(
        full_units=monetary_integer // 100,
    )
