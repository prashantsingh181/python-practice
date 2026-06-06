class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner}'s account: ${self.balance}"

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("amount should be either int or float")

        if amount <= 0:
            raise Exception("Amount should be greater than 0")
        elif amount > self.balance:
            raise Exception("Insufficient Funds")

        self.balance -= amount
        print(f"${amount} withdrawn from {self.owner}'s account")

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("amount should be either int or float")

        if amount <= 0:
            raise Exception("Amount should be greater than 0")

        self.balance += amount
        print(f"${amount} deposited in {self.owner}'s account")


acc = BankAccount("Alice", 100)
acc.deposit(50)
acc.withdraw(10)
print(acc)
