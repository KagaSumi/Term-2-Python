import pytest
from bank import BankAccount


def test_account_has_property_amount():
    assert type(BankAccount.amount) == property


def test_amount_zero():
    account = BankAccount()
    assert account.amount == 0


def test_amount_setter():
    account = BankAccount()

    account.amount = 100
    account.deposit(10)
    account.withdraw(1)
    assert account.amount == 109

    with pytest.raises(ValueError):
        # Cannot set the account amount to a negative value!
        account.amount = -5


def test_withdraw():
    account = BankAccount()

    account.deposit(1000)

    with pytest.raises(ValueError):
        # You cannot withdraw more than you have!
        account.withdraw(2000)
