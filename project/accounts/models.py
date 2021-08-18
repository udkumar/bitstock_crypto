from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Account(models.Model):
    """
    Client account to hold currency
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    # Saving balance into satoshis
    balance = models.IntegerField('balance', default=0)
    updated_on = models.DateTimeField(default=now)


class Transaction(models.Model):
    """
    Transaction explaining the change of an account balance: deposits, withdrawal, etc.
    """
    TRANSACTION_TYPE_DEPOSIT = 1
    TRANSACTION_TYPE_WITHDRAWAL = 2

    transaction_type = models.PositiveIntegerField(
        'transaction_type',
        choices=(
            (TRANSACTION_TYPE_DEPOSIT, 'deposit'),
            (TRANSACTION_TYPE_WITHDRAWAL, 'withdrawal'),
        )
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')

    # removed FloatField because when there's enough rounding involved it may not matter, but for money we really can't have rounding errors
    # Saving txn amount into satoshis
    amount = models.IntegerField('amount', default=0)
    created_on = models.DateTimeField(default=now, editable=False)