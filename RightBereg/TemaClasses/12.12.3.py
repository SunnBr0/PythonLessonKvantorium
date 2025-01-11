class BankAccount:
    def __init__(self,name,balance = 0):
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
    def withdraw (self,amount):
        if self.__balance>=amount>0:
            self.__balance -=amount
    def getBalance(self):
        return self.__balance
myAccount = BankAccount("Oleg",100)
print("Баланс", myAccount.getBalance())
myAccount.deposit(33)
print("Баланс", myAccount.getBalance())
myAccount.withdraw(123)
print("Баланс", myAccount.getBalance())