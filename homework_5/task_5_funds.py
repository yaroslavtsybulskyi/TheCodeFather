class InsufficientFundsException(Exception):
    """
    Exception raised when an insufficient funds are requested
    """

    def __init__(self, required_amount: int | float, current_balance: int | float,
                 currency: str, transaction_type: str) -> None:
        """
        Constructor
        :param required_amount: amount of transaction
        :param current_balance: current amount on balance
        :param currency: currency of transaction
        :param transaction_type: type of transaction
        """
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type
        self.message = (f"You are {self.required_amount - self.current_balance} {self.currency} "
                        f"short for {self.transaction_type}")
        super().__init__(self.message)


class BankAccount:
    """
    Bank account class
    """

    def __init__(self, amount: int | float, currency: str = 'UAH') -> None:
        """
        Constructor
        :param amount: amount on bank account
        :param currency: currency of account
        """
        self.amount = amount
        self.currency = currency

    def spend(self, amount: int | float, currency: str = 'UAH') -> None:
        """
        Spending method
        :param amount: amount to spend
        :param currency: currency of transaction
        :return:
        """
        if amount < 0:
            raise ValueError('Amount must be positive')

        if self.currency != currency:
            print(f"Transaction can be completed in same currency only.")

        if amount > self.amount:
            raise InsufficientFundsException(amount, self.amount, self.currency, "Purchase")

        self.amount -= amount

    def withdraw_atm(self, amount: int | float, currency: str = 'UAH') -> None:
        """
        Cash withdrawal method
        :param amount: amount of the withdrawal
        :param currency: currency of transaction
        :return:
        """
        if amount < 0:
            raise ValueError('Amount must be positive')

        if self.currency != currency:
            print(f"Transaction can be completed in same currency only.")

        if amount > self.amount:
            raise InsufficientFundsException(amount, self.amount, self.currency, "ATM Withdrawal")

        self.amount -= amount


if __name__ == '__main__':
    try:
        account = BankAccount(100)
        account.spend(100)
        account.withdraw_atm(100)
    except InsufficientFundsException as e:
        print(e)

    try:
        account = BankAccount(100, "USD")
        account.spend(100, "UAH")
        account.spend(150.6, "USD")
    except (InsufficientFundsException, ValueError) as e:
        print(e)
