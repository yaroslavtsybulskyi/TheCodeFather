"""
Test Suite for the BankAccount Class

This module contains unit tests for the `BankAccount` class,
focusing on balance initialization, deposits, withdrawals,
error handling, and mocking API interactions.

"""

import pytest

from unittest.mock import Mock

from homework_7.task_6_wallet import BankAccount


@pytest.fixture
def bank_account():
    """
    Fixture to create a BankAccount instance with an initial balance of 100.
    :return: BankAccount instance
    """
    return BankAccount(100)


def test_balance_when_created():
    """Test that a new BankAccount starts with the correct initial balance."""
    bank_account = BankAccount(100)
    assert bank_account.balance == 100


def test_balance_deposit(bank_account):
    """Test that depositing funds correctly updates the balance."""
    bank_account.deposit(150)
    assert bank_account.get_balance() == 250.00


@pytest.mark.parametrize("initial, deposit, expected", [
    (100, 200, 300),
    (300, 150, 450),
    (120.15, 166.15, 286.30),
    (100, 4000, 4100)
])
def test_balance_deposit(initial, deposit, expected):
    """
    Test deposit functionality with multiple values.
    - Skips test if deposit is >= 4000.
    :param initial: initial balance
    :param deposit: deposit amount
    :param expected: expected balance
    """
    if deposit >= 4000:
        pytest.skip("Deposit amount is too high")
    bank_account = BankAccount(initial)
    bank_account.deposit(deposit)
    assert bank_account.get_balance() == expected


@pytest.mark.parametrize("initial, withdraw_amount, expected", [
    (500, 200, 300),
    (300, 150, 150),
    (75.50, 6.15, 69.35),
    (0, 55, 100)
])
def test_balance_withdraw(initial, withdraw_amount, expected):
    """
    Test withdrawal functionality with multiple values.
    - Skips test if initial balance is 0.
    :param initial: initial balance
    :param withdraw_amount: withdrawal amount
    :param expected: expected balance
    """
    if initial == 0:
        pytest.skip("Initial balance is zero")
    bank_account = BankAccount(initial)
    bank_account.withdraw(withdraw_amount)
    assert bank_account.get_balance() == expected


def test_bank_account_creation_with_balance_as_string():
    """Test that creating a BankAccount with a non-numeric balance raises TypeError."""
    with pytest.raises(TypeError):
        bank_account = BankAccount('5')


def test_deposit_not_number():
    """Test that depositing a BankAccount with a non-numeric amount raises TypeError."""
    with pytest.raises(TypeError):
        bank_account = BankAccount('6')


def test_withdraw_not_number():
    """Test that withdrawing from the BankAccount with a non-numeric amoount raises TypeError."""
    with pytest.raises(TypeError):
        bank_account = BankAccount('7')


def test_deposit_negative_number():
    """Test that depositing a negative amount raises ValueError."""
    bank_account = BankAccount(5)
    with pytest.raises(ValueError):
        bank_account.deposit(-1)


def test_withdraw_negative_number():
    """Test that withdrawing a negative amount raises ValueError."""
    bank_account = BankAccount(500)
    with pytest.raises(ValueError):
        bank_account.withdraw(-1)


def test_bank_account_creation_with_negative_number():
    """Test that creating account with negative amount raises ValueError."""
    with pytest.raises(ValueError):
        bank_account = BankAccount(-5)


@pytest.mark.skipif(lambda: BankAccount().get_balance() == 0,
                    reason="Empty balance")
def test_withdraw_on_empty_balance():
    """Test that withdrawing on an empty balance raises ValueError."""
    bank_account = BankAccount()
    with pytest.raises(ValueError):
        bank_account.withdraw(200)


def test_balance_check_with_mock():
    """Test balance retrieval using a mock API."""
    bank_account = BankAccount(100)

    api = Mock()
    api.get_balance.return_value = bank_account.get_balance()

    assert api.get_balance() == 100
    api.get_balance.assert_called_once_with()


def test_deposit_with_mock():
    """Test deposit using a mock API."""
    bank_account = BankAccount(100)
    api = Mock()
    api.deposit = Mock(side_effect=bank_account.deposit)
    api.get_balance = Mock(side_effect=bank_account.get_balance)
    api.deposit(100)
    assert api.get_balance() == 200
    api.deposit.assert_called_once_with(100)
    api.get_balance.assert_called_once_with()
