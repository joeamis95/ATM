from Account import Account


class BusinessAccount(Account):
    def __init__(self, deposit, withdrawal, balance):
        Account.__init__(self, balance)
        self.deposit = deposit
        self.withdrawal = withdrawal
        self.balance = balance

    def userBusinessWithdrawal(self):
        amount_withdraw = self.withdraw()
        print(amount_withdraw)
        return amount_withdraw

    def userBusinessDeposit(self):
        amount_deposit = self.depositing()
        print(amount_deposit)
        return amount_deposit

    def businessBalance(self):
        print(self.balance)
        return self.balance
