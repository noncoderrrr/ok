class BankAccount:
    def __init__(self,AccountHolderName,BankBalance):
        self.AccountHolderName=AccountHolderName
        self.BankBalance=BankBalance
        print("account created successfully.")
    def deposit(self):
        while True:
            try:
                amount=int(input("enter amount to deposit:"))
                if amount>=0:
                    self.BankBalance=self.BankBalance+amount
                    print("amount deposited successfully. current bank balance:",self.BankBalance)
                else:
                    print("enter positive amount")
                break
            except ValueError:
                print("enter whole number")
    def withdraw(self):
        while True:
            try:
                amount=int(input("enter amount to withdraw:"))
                if amount<=self.BankBalance and amount>=0:
                    self.BankBalance=self.BankBalance-amount
                    print("amount withdrawal was done successfully. current bank balance:",self.BankBalance)
                elif amount>self.BankBalance:
                    print("insufficient funds")
                else:
                     print("enter a positive amount")
                break
            except ValueError:
                print("enter whole number")
    def GetAccountInfo(self):
        print("account holder's name:",self.AccountHolderName,". current bank balance:",self.BankBalance)
    def GetBalance(self):
        print("current bank balance:",self.BankBalance)
name=str(input("enter account holder's name:"))
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
    
