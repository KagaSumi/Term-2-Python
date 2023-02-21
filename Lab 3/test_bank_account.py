import pytest
from bank import BankAccount


@pytest.fixture
def bank_account():
    account = BankAccount()
    account.deposit(1000)
    return account


def test_amount_zero():
    account = BankAccount()
    assert account.amount == 0


def test_deposit():
    account = BankAccount()

    account.deposit(1000)
    assert account.amount == 1000


def test_deposit_with_fixture(bank_account):
    assert bank_account.amount == 1000
    bank_account.deposit(1000)
    assert bank_account.amount == 2000


def test_withdraw():
    account = BankAccount()

    account.deposit(1000)
    assert account.amount == 1000

    account.withdraw(500)
    assert account.amount == 500


def test_withdraw_more_than_available(bank_account):
    with pytest.raises(ValueError):
        # You cannot withdraw more than you have!
        bank_account.withdraw(2000)
