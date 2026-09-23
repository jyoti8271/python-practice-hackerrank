class payment:
    def pay(self):
        pass
    
class creditcard(payment):
    def pay(self):
        print("payment through credit card")
        
class debitcard(payment):
    def pay(self):
        print("payment through debit card")
        
        
class cash(payment):
    def pay(self):
        print("payment through cash")
        
payment1=[creditcard(),debitcard(),cash()]

for payment in payment1:
    payment.pay()
    
            
    