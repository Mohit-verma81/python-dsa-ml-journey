class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        print(f"Balance: {self.balance}")


# Usage
account = BankAccount("Titan", 1000)
account.deposit(500)
account.withdraw(300)
account.check_balance()