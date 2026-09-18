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
    
    
## new question
try:
    num=int(input("enter the new age"))
    result=10/num
    
except ValueError:
    print("this is not a vlaid number")
    
except ZeroDivisionError:
    print("enter denominator greater than 0")
    
except Exception as ex:
    print("hii")
    

##try,except, else block
try:
    num=int(input("enter the number"))
    result=1/num
    
except ValueError:
    print("this is not a vlaid number")
except ZeroDivisionError:
    print("you can't divide by zero")

except Exception as ex:
    print("ex")
    
else:
    print(f"the result is{result}")   
    



#try,except,else,finally
b 













    