class BankAccount:
    def __init__(self,name,balance = 0):
        self.name = name
        self.__balance = balance
    def deposit(self,money):
        if money > 0:
            self.__balance += money
    def withdraw (self,money):
        if self.__balance >= money >0 :
            self.__balance -= money
    def getBalance(self):
        return self.__balance
OlegAccount = BankAccount("Oleg",100)
print("Баланс",OlegAccount.getBalance())
OlegAccount.deposit(35)
print("Баланс",OlegAccount.getBalance())
OlegAccount.withdraw(125)
print("Баланс",OlegAccount.getBalance())