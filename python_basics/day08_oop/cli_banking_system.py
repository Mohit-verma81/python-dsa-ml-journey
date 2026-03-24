class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")

    def show_balance(self):
        print(f"Current Balance: {self.balance}")


account = BankAccount("User", 1000)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Balance\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")