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
try:
    num=int(input("enter the number"))
    result=1/num
    
except ValueError:
    print("this is not a vlaid number")
except ZeroDivisionError:
    print("you can't divide by zero")
    #base case

except Exception as ex:
    print("ex")
    
else:
    print(f"the result is{result}") 
    
finally:
    print("execution complete")
    
    
###custom exception handling

class Error(Exception):
    pass
class dobExceptioon(Error):
    pass

try:
    year=int(input("enter the year"))
    age=2024-year
    if age<=30 and age>=20:
        print("the age is valid you can apply for the vote")
    else:
        raise dobExceptioon
    
except dobExceptioon:
    print("your age sould be greater than 20")
    
finally:
    print("sorry your age should be graeter than 20 and less than 30")
    
    
##real world use case on file handling 
try:
    file=open("example.txt",'r')
    content=file.read()
    print(content)
    
except FileNotFoundError:
    print("the file does not exist")
    
finally:
    if 'file' in locals () and not file.closed():
        file.close()
        
    print('file close')
    
    
    












    