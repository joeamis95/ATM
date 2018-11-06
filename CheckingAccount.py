from Account import Account


class CheckingAccount(Account):
    def __init__(self, deposit, withdrawal, balance):
        Account.__init__(self, balance)
        self.deposit = deposit
        self.withdrawal = withdrawal
        self.balance = balance

    def userCheckingWithdrawal(self):
        amount_withdraw = self.withdraw()
        print(amount_withdraw)
        return amount_withdraw

    def userCheckingDeposit(self):
        amount_deposit = self.deposit()
        print(amount_deposit)
        return amount_deposit

    def checkingBalance(self, balance):
        print(balance)
        return balance
