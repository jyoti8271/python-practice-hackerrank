class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
        
    def add(self):
        return self.num1+ self.num2
    
    def subtract(self):
        return self.num1-self.num2
    
    
    def multiply(self,factor):
        return self.num1*factor
    
    
    def divide(self,divisor):
        if divisor==0:
            print("error:cannot divide by zero")
            
        else:
            return self.num1/divisor
        
        
calculator1=calculator(9,7)
print("addition result",calculator1.add())
print("substraction result",calculator1.subtract())
print("multiply result",calculator1.multiply(9))
print("divide result",calculator1.divide(4))
        