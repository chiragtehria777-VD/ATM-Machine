class Account:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def get_balance(self):
        return self.balance

    def update_balance(self, amount):
        self.balance += amount

    def add_transaction(self, message):
        self.transactions.append(message)

    def get_transactions(self):
        return self.transactions