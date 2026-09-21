class bank_account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
        
    def deposit(self,amount):
        self.balance+=amount
        
    
    def withdraw(self,amount):
        self.balance-=amount
        
    
    def transfer(self,other_account,amount):
        self.balance -= amount
        other_account.balance+=amount
        
        
acc1=bank_account("john Doe",1000)
acc2=bank_account("jane Smith",2000)

acc1.deposit(500)
acc1.withdraw(100)
acc1.transfer(acc2,80)

print(acc1.balance)
print(acc2.balance)        