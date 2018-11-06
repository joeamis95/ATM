from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount
from BusinessAccount import BusinessAccount

def userPrompt():
        checking_account = CheckingAccount(200, 500, 1000)
        savings_account = SavingsAccount(10, 400, 200)
        business_account = BusinessAccount(20, 10, 400)

        name = input("Hello. Welcome to Joe's First Class Banking System. Please enter your name.\n")
        answer = input("Hi " + name + ", would you like to make a new account with us?\n")

        if answer.lower() in ['y', 'yes']:
            print("Great! How can I help you?\n")
        else:
            return exit("Well I guess you don't want to bank with us :( Peace Out!")

        key = input("Type:\n[W]ithdraw\n[D]eposit\n[B]alances\n[Q]uit\n")

        if key.lower() == 'w':
            option = input("Choose an account:\n[C]hecking\n[S]avings\n[B]usiness\n")
            if option.lower() == 'c':
                return checking_account.userCheckingWithdrawal()
            elif option.lower() == 's':
                return savings_account.userSavingsWithdrawal()
            elif option.lower() == 'b':
                return business_account.userBusinessWithdrawal()
            else:
                return key
        if key.lower() == 'd':
            option = input("Choose an account:\n[C]hecking\n[S]avings\n[B]usiness\n")
            if option.lower() == 'c':
                return checking_account.userCheckingDeposit
            elif option.lower() == 's':
                return savings_account.userSavingsDeposit()
            elif option.lower() == 'b':
                return business_account.userBusinessDeposit()
            else:
                return key
        if key.lower() == 'b':
            option = input("Choose an account:\n[C]hecking\n[S]avings\n[B]usiness\n")
            if option.lower() == 'c':
                return checking_account.checkingBalance()
            elif option.lower() == 's':
                return savings_account.savingsBalance()
            elif option.lower() == 'b':
                return business_account.businessBalance()
            else:
                return key
        if key.lower() == 'q':
            return exit("Thank you for visiting Joe's First Class Banking System! Come back soon!")


userPrompt()
