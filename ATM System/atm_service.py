from account import Account
from statement import print_statement

class ATMService:
    def __init__(self):
        self.account = Account()

    def display_balance(self):
        print(f"\nCurrent Balance: ₹{self.account.get_balance()}")

    def deposit(self, amount):
        if amount > 0:
            self.account.update_balance(amount)
            self.account.add_transaction(f"Deposited ₹{amount}")
            print("Deposit successful!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.account.get_balance():
            print("Insufficient balance!")
        else:
            self.account.update_balance(-amount)
            self.account.add_transaction(f"Withdrawn ₹{amount}")
            print("Withdrawal successful!")

    def show_statement(self):
        print_statement(self.account.get_transactions())