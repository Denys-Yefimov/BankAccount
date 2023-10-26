class BankAccount:

    def __init__(self):
        self.withdrawals = 0
        self.replenishment = 0
        self.account = 0

    def replenish(self):
        self.account += self.replenishment
        print(f"You have replenishment ${self.replenishment} your account")

    def withdraw(self):
        if self.withdrawals <= self.account:
            self.account -= self.withdrawals
            print(f"You have withdrawn ${self.withdrawals} from your account")
        else:
            print("You don`t have enough funds in your account")

    def __str__(self):
        print(f"BankAccount {self.account}")


my_account = BankAccount()


while True:
    print("Welcome to UNIVERSAL BANK 'manobank'")
    print("if you to make a replenishment press 1")
    print("if you to make a withdraw press 2")
    button_for_operations = input()
    if button_for_operations == "1":
        my_account.replenishment = int(input("How much do you want to replenish your account? "))
        my_account.replenish()
    elif button_for_operations == "2":
        my_account.withdrawals = int(input("How much do you want to withdraw? "))
        my_account.withdraw()
    BankAccount.__str__(my_account)
