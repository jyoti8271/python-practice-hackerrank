
#for acessing the private variable we used the get method
class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
        
    def get_balance(self):
        return(self.__balance)
        
        
account1=bankaccount(1000)
account1.get_balance()



##for changing the value of private variable we used the set method

class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,balance):
        if balance>=0:
            self.__balance=balance
            
            
        else:
            print("balance canot be negative")
            
account2=bankaccount(10000)

print(account2.get_balance())

account1.set_balance(150000)
print(account2.get_balance)


###protected variable
class parent:
    def __init__(self):
        self.salary=5000
        
class child(parent):
    def show(self):
        print(self._salary)
        
        
obj=child()
obj.show()



##private varibale +inheritence

class parent:
    def __init__(self):
        self.__salary=500000
        
obj=parent()
print(obj._parent__salary)
        
        