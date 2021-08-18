from .models import Account, Transaction
import datetime


def perform_deposit(user, amount):
    try:
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
    except:
        print("Something went wrong with amount deposit")

def perform_withdrawal(user, amount):
    try:
        amount = btc_to_satoshis(amount)
        account = Account.objects.get(user=user)
        if account:
            transaction = Transaction.objects.create(
                account=account,
                amount=amount,
                transaction_type=Transaction.TRANSACTION_TYPE_WITHDRAWAL
            )
            if transaction:
                account.balance -= amount
                account.updated_at = datetime.datetime.now
                account.save()

            return transaction
    except:
        print("Something went wrong with withdrawal")

def btc_to_satoshis(btc):
    satoshis = btc*100000000
    return satoshis

def satoshis_to_btc(satoshis):
    btc = satoshis/100000000
    return btc