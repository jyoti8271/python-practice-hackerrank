class car :
    pass

audoi=car()
bmw=car()
tata=car()
print(type(audoi))

audoi.windows=4
print(audoi.windows)

tata.door=3
print(tata.door)







#2.instance varibale and method
class dog:
    #constructor
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        

##create object        
dog1=dog("herry",5)
dog2=dog('jerry',4)
print(dog)
print(dog1.age)
print(dog2.name)



#3.define a class with method
class dog:
    #constructor call
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        
    #instance method
    def bark(self):
        print(f"{self.name}says woof")
        
#cretae an object
dog1=dog("buddy",4)
dog2=dog("numan",6)
print(dog1)
print(dog2)
dog1.bark()
dog2.bark()


#4.Modelling a bank account 
#define a class from bank account
class bankaccount:
    #constructor call
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        
    #instance method
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited in your account, new balance is {self.balance}")
        
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient fund")
            
        else:
            self.balance-=amount
            print(f"{amount} is withdraw,new balnce is {self.balance}")
            
    def get_balance(self):
        return self.balance
    
#create an object
account1=bankaccount("aman",7000)
print(account1)
print(account1.balance)

##call instance method

account1.deposit(100)
account1.withdraw(90)

print(account1.get_balance())




            
        
        
    
    


        
        






