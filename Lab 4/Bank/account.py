from customer import Customer


class Account:
    """
    A class to represent a bank.
    """
    def __init__(self, owner:Customer, amount:int=0) -> None:
        if not isinstance(owner, Customer):
            raise AttributeError
        self.owner = owner
        self.amount = amount

    def deposit(self, amount:int or float) -> None:
        """Adds amount to accounts amount

        Args:
            amount (int or float): Amount to be deposited

        Raises:
            AttributeError: Thrown if amount is not positive
        """
        if amount < 0:
            raise AttributeError('Cannot deposit negative amount')
        self.amount += amount

    def withdraw(self, amount:int or float) -> None:
        """Removes the amount from the account's amount

        Args:
            amount (int or float): Amount to be withdrew

        Raises:
            AttributeError: Thrown if amount is not positive
        """
        if amount < 0:
            raise AttributeError('Cannot withdraw negative amount')
        self.amount -= amount

    def transfer(self, trans_acc, amount:int or float) -> None:
        """Transfers balance from this account to another account

        Args:
            trans_acc (Account): This is another instance of the account object
            amount (int or float): The amount to transfer from this account to the trans_acc

        Raises:
            TypeError: Raises Typeerror if trans_acc is not an instance of Account
        """
        if not isinstance(trans_acc, Account):
            raise TypeError('trans_acc must be an instance of Account')
        self.withdraw(amount)
        trans_acc.deposit(amount)


class CreditAccount(Account):
    def __init__(self, cus, rate):
        super().__init__(cus)
        self.interest = rate

    def compute_interest(self) -> None:
        """Adds interest and $10 fee to the account if balance is not positive.
        """        
        if self.amount < 0:
            self.amount *= (100+self.interest)/100
            self.amount -= 10


class SavingsAccount(Account):
    def __init__(self, cus):
        super().__init__(cus)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise UserWarning
        self._amount = value
