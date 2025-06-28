class BankAccount:
    def __init__(self,account_holder_name,bank_balance):
        self.account_holder_name=account_holder_name
        self.bank_balance=bank_balance
        print("account created successfully.")
    def deposit(self):
        while True:
            try:
                amount=int(input("enter amount to deposit:"))
                if amount>0:
                    self.bank_balance=self.bank_balance+amount
                    print("amount deposited successfully. current bank balance:",self.bank_balance)
                    break
                else:
                    print("enter positive amount")
            except ValueError:
                print("enter whole number")
    def withdraw(self):
        while True:
            try:
                amount=int(input("enter amount to withdraw:"))
                if amount<=self.bank_balance and amount>0:
                    self.bank_balance=self.bank_balance-amount
                    print("amount withdrawal was done successfully. current bank balance:",self.bank_balance)
                    break
                elif amount>self.bank_balance:
                    print("insufficient funds")
                else:
                     print("enter a positive amount")
            except ValueError:
                print("enter whole number")
    def get_account_info(self):
        print("account holder's name:",self.account_holder_name,". current bank balance:",self.bank_balance)
    def get_balance(self):
        print("current bank balance:",self.bank_balance)
name=input("enter account holder's name:")
while True:
    try:
        balance=int(input("enter bank balance:"))
        if balance>=0:
            acc1=BankAccount(name,balance)
            break
        else:
            print("enter valid number")
    except ValueError:
        print("enter whole number")
print("what would you like to do today?")
print("click 1 to get account info")
print("click 2 to deposit amount")
print("click 3 withdraw amount")
print("click 4 to view bank balance")
print("click 5 to exit")
while True:
    try:
        ask=int(input("pick a choice from 1-5:"))
        if ask==1:
            acc1.get_account_info()
        elif ask==2:
            acc1.deposit()
        elif ask==3:
            acc1.withdraw()
        elif ask==4:
            acc1.get_balance()
        elif ask==5:
            print("thank you!")
            break
        else:
            print("enter a number from 1-5")
    except ValueError:
        print("enter a number from 1-5")
