from datetime import datetime


class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def validate(self):
        pass

    def has_sufficient_balance(self, amount):
        return self.balance >= amount

    def debit(self, amount):
        if self.has_sufficient_balance(amount):
            self.balance -= amount

    def credit(self, amount):
        self.balance += amount


class Transfer:

    def __init__(self, from_account: Account, to_account: Account, amount: float):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.transaction_date = datetime.now()
