"""
Bank Account Management Module

This module provides a `BankAccount` class for managing financial transactions,
including deposits, withdrawals, and balance retrieval.

Classes:
    - BankAccount: Handles account balance operations.
"""


class BankAccount:
    """A class representing a bank account with basic financial operations."""

    def __init__(self, balance: float = 0.0):
        """
        Initializes the bank account with a given balance.
        :param balance: Initial account balance (default: 0.0).
        :raises TypeError: If `balance` is not a number.
        """
        if not isinstance(balance, (int, float)):
            raise TypeError("Balance must be a number (int or float)")
        if balance < 0:
            raise ValueError('Balance cannot be negative')
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Deposits an amount into the account.

        :param amount: The amount to be added to the account.
        :raises ValueError: If the deposit amount is negative.
        :raises TypeError: If the deposit amount is not a number.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number (int or float)")
        if amount < 0:
            raise ValueError('Deposit amount cannot be negative')
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraws an amount from the account if funds are available.
        :param amount: The amount to be withdrawn.
        :raises ValueError: If withdrawal amount is negative or exceeds balance.
        :raises TypeError: If withdrawal amount is not a number.
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number (int or float)")
        if amount < 0:
            raise ValueError('Withdraw amount cannot be negative')
        if amount > self.balance:
            raise ValueError('Not enough funds')
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Returns the current balance of the account.
        :return: The account balance as a float.
        """
        return self.balance
