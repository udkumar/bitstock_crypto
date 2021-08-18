from .models import Account, Transaction
import datetime


def perform_deposit(user, amount):
    amount = btc_to_satoshis(amount)
    account = Account.objects.get(user=user)
    if account:
        transaction = Transaction.objects.create(
            account=account,
            amount=amount,
            transaction_type=Transaction.TRANSACTION_TYPE_DEPOSIT
        )
        if transaction:
            account.balance += amount
            account.updated_at = datetime.datetime.now
            account.save()

        return transaction

def perform_withdrawal(user, amount):
    pass

def btc_to_satoshis(amount):
    amount = amount*100000000
    return amount