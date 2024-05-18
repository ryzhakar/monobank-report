from django.contrib import admin

from server.apps.main import models


@admin.register(models.ClientInfo)
class ClientInfoAdmin(admin.ModelAdmin[models.ClientInfo]):
    """Admin representation."""
    list_display = ('client_id', 'name', 'token')
    search_fields = ('client_id', 'name')


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin[models.Account]):
    """Admin representation."""
    list_display = (
        'client_id',
        'account_type',
        'balance',
        'credit_limit',
        'currency_code',
        'last_sync_at',
    )
    search_fields = ('id', 'send_id', 'account_type', 'currency_code', 'iban')
    list_filter = ('account_type', 'currency_code', 'cashback_type')


@admin.register(models.StatementItem)
class StatementItemAdmin(admin.ModelAdmin[models.StatementItem]):
    """Admin representation."""
    list_display = (
        'description',
        'account_id',
        'time',
        'mcc',
        'amount',
        'currency_code',
        'balance',
        'comment',
    )
    search_fields = (
        'id',
        'description',
        'mcc',
        'original_mcc',
        'currency_code',
        'receipt_id',
        'invoice_id',
        'counter_edrpou',
        'counter_iban',
        'counter_name',
    )
    list_filter = (
        'account__client',
        'account__account_type',
        'account__currency_code',
    )
