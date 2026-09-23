class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
        
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,value):
        if value>=0:
            self.balance=value
            
        else:
            print("invalid balance")
            
            
account=bankaccount()
print(account.balance())

account.balance=20000
print(account.balance)



###this concept using python concept
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")

        elif amount > self.__balance:
            print("Insufficient balance")

        else:
            self.__balance -= amount
            print("Withdrawal successful")

    def get_balance(self):
        return self.__balance


account = BankAccount(10000)

account.withdraw(3000)

print(account.get_balance())