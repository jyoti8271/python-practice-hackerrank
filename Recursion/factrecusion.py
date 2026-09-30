import sys

def factorial(n):
    smallans=factorialfour(n-1)
    ans=n*smallans
    return ans

def factorialfour(n):
    smallans=factorialthree(n-1)
    ans=n*smallans
    return ans


def factorialthree(n):
    smallans=factorialtwo(n-1)
    ans=n*smallans
    return ans

def factorialtwo(n):
    smallans=factorialone(n-1)
    ans=n*smallans
    return ans

def factorialone(n):
    return 1

print(factorial(5))









##by using base case
def factorial(n):
    if n<=1:
        return 1
    
    smallans=factorial(n-1)
    ans=n*smallans
    return ans

print(factorial(5))


##another method
import math
print(math.factorial(5))

##another method---> incresing order
def factorial(num):
    ans=1
    
    for i in range (1,num+1):
        ans=ans*i
    return ans
print(factorial(7))


def faactorial(n):
    ans=1
    for i in range(n,0,-1):
        ans=ans*i
    return ans
print(faactorial(8))
        


    