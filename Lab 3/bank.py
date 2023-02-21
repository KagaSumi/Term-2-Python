class BankAccount:
    def __init__(self):
        self._amount = 0
    def deposit(self,value):
        self._amount += value
    def withdraw(self,value):
        if self._amount - value < 0:
            raise ValueError
        self._amount -= value
        
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError
        self._amount = value