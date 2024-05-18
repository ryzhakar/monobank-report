from django.db import models


class MerchantCategoryCode(models.Model):
    """Merchant category code."""
    code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)
    of_interest = models.BooleanField(default=False)

    class Meta:
        """Override naming."""
        verbose_name = 'Merchant Category Code'
        verbose_name_plural = 'Merchant Category Codes'

    def __str__(self) -> str:
        """Provide string representation."""
        return self.description


class ClientInfo(models.Model):
    """Monobank client info and a token."""
    client_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=255)

    class Meta:
        """Override table definition."""
        db_table = 'client_info'
        verbose_name = 'Client Info'
        verbose_name_plural = 'Client Info'

    def __str__(self) -> str:
        """Provide string representation."""
        return self.name


class Account(models.Model):
    """A clients account."""
    id = models.CharField(max_length=255, primary_key=True)
    send_id = models.CharField(max_length=255)
    balance = models.BigIntegerField()
    credit_limit = models.BigIntegerField()
    account_type = models.CharField(max_length=255)
    currency_code = models.IntegerField()
    cashback_type = models.CharField(max_length=255, null=True, blank=True)
    iban = models.CharField(max_length=255, null=True, blank=True)
    last_sync_at = models.DateTimeField(null=True, blank=True)
    client = models.ForeignKey(
        ClientInfo, related_name='accounts', on_delete=models.CASCADE,
    )

    class Meta:
        """Override table definition."""
        db_table = 'accounts'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self) -> str:
        """Provide string representation."""
        return self.id


class StatementItem(models.Model):
    """A single transaction associated with an account."""
    id = models.CharField(max_length=255, primary_key=True)
    account = models.ForeignKey(
        Account, related_name='statement_items', on_delete=models.CASCADE,
    )
    time = models.DateTimeField()
    description = models.TextField()
    mcc = models.IntegerField()
    original_mcc = models.IntegerField()
    hold = models.BooleanField()
    amount = models.BigIntegerField()
    operation_amount = models.BigIntegerField()
    currency_code = models.IntegerField()
    commission_rate = models.BigIntegerField()
    cashback_amount = models.BigIntegerField()
    balance = models.BigIntegerField()
    comment = models.TextField(null=True, blank=True)
    receipt_id = models.CharField(max_length=255, null=True, blank=True)
    invoice_id = models.CharField(max_length=255, null=True, blank=True)
    counter_edrpou = models.CharField(max_length=255, null=True, blank=True)
    counter_iban = models.CharField(max_length=255, null=True, blank=True)
    counter_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        """Override table definition."""
        db_table = 'statement_items'
        verbose_name = 'Statement Item'
        verbose_name_plural = 'Statement Items'

    def __str__(self) -> str:
        """Provide string representation."""
        return self.id
