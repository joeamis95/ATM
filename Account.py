class Account:
    def __init__(self, money, balance=1000000):
        self.balance = balance
        self.money = money

    def withdraw(self):
        amount = int(input("How much do you want to withdraw?\n"))
        self.balance -= amount
        return self.balance

    def depositing(self):
        amount = int(input("How much do you want to deposit?\n"))
        self.balance += amount
        return self.balance
