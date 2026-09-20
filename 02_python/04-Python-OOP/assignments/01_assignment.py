class BankAccount:
    
    def __init__(self,account_number,owner_name,balance):
        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance

    def deposit(self,new_balance):
        self.balance +=new_balance


    def withdraw(self,withdraw_balance):
        self.balance -=withdraw_balance


    def check_balance(self):
        return self.balance




acc1=BankAccount(13580110160480,"Dibyaranjan Das",1000)
acc1.deposit(359)
acc1.withdraw(765)
print(f"total balance={acc1.check_balance()}")





