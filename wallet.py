class Wallet:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(f"Balance: {self.balance}")
