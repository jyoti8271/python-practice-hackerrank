try:
    a=b
    
except NameError as ex:
    print("the variable is not assigned")
    print(ex)




try:
    a=b
    
except:
    print("the variable has not been assigned")





#zero-Divison Error

try:
    result=1/0
    
except ZeroDivisionError as ex:
    print(ex)
    
    print("please enter the denominator greater than 0")




 ##base class as an exception
try:
    result=1/2
    a=b
    
except ZeroDivisionError as ex:
    print(ex)
    print("please enter the denominator greater than 0")
    
except Exception as ex1:
    
    print("main exception can caught here")











    