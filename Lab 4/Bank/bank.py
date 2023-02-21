from customer import Customer
from account import Account as account
from account import CreditAccount as credit
from account import SavingsAccount as savings


class Bank:
    """
    A class to represent a bank.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    accounts : list
        family name of the person

    Methods
    -------
    create_account(self, category:str, owner: Customer, interest_rate: int =0) -> account
        Creates a new account for the a new or existing client
        this requires a specification on what type of account is being made
    find_accounts_by_ssn(self, ssn:str) -> list[account]
        returns a list of accounts that is associated with that SSN
    find_accounts_by_name(self, name:str) -> list[account]
        returns a list of accounts that is associated with that name
    """

    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, category: str, owner: Customer, interest_rate: int = 0) -> account:
        """Creates a new account for the a new or existing client
        this requires a specification on what type of account is being made

        Args:
            category (str): A string describing the category of account being created
            owner (Customer): A Customer object representing the owner of the account
            interest_rate (int, optional): This is a interest rate that is a percentage
            represented as an int. Defaults to 0.

        Raises:
            AttributeError: If the owner is not a customer object there will be a AttributeError
            ValueError: Interest rate must be within 0 to 100

        Returns:
            account: Account object for the account created
        """
        if not isinstance(owner, Customer):
            raise AttributeError
        if not 0 <= interest_rate <= 100:
            raise ValueError('Interest rate must be within 0 to 100')
        if category == "account":
            new_account = account(owner)
            self.accounts.append(new_account)
            return new_account

        elif category == "credit":
            new_account = credit(owner, interest_rate)
            self.accounts.append(new_account)
            return new_account

        elif category == "savings":
            new_account = savings(owner)
            self.accounts.append(new_account)
            return new_account

    def find_accounts_by_ssn(self, ssn: str) -> list[account]:
        """Takes in a a SSN and returns a list of accounts that is associated
        with that SSN.

        Args:
            ssn (str): SSN associated with a client to the bank

        Returns:
            list[account]: A list of accounts that are associated with SSN
        """
        cus_accounts = []
        for acc in self.accounts:
            if acc.owner.ssn == ssn:
                cus_accounts.append(acc)
        return cus_accounts

    def find_accounts_by_name(self, name: str) -> list[account]:
        """Function Takes in a Name and returns a list of Accounts that is
        associated with that name

        Args:
            name (str): Name of a client at the bank

        Returns:
            list[account]: List of Accounts that are associated with the name
        """
        cus_accounts = []
        for acc in self.accounts:
            if acc.owner.name == name:
                cus_accounts.append(acc)
        return cus_accounts

    @property
    def balance(self):
        total = 0
        for acc in self.accounts:
            total += acc.amount
        return total
