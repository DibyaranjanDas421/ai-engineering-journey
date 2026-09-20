class BankAccount:
    def __init__(self,name,balance):
        self.name=name #public
        self.__balance=balance # private (_,single for protected)


    def get_balance(self):
        return self.__balance

    def set_balance(self,newBalance):
        self.__balance=newBalance  


acc1=BankAccount("Dibya",100_000)

print(acc1.name,acc1.get_balance())

