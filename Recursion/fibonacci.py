def fibo(num):
    if num==0:
        return 0
    if num==1:
        return 1
    
    last=fibo(num-1)
    secondlast=fibo(num-2)
    ans=last+secondlast
    return ans
    
print(fibo(9))
    