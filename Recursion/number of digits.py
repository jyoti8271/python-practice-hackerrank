#123--->3
#48765---->5
def sumofdigit(n):
    #base case
    if n>=0 and n<=9:
        return 1
    smallans=sumofdigit(n//10)
    ans=1+smallans
    return ans

print(sumofdigit(17))
print(sumofdigit(171))
print(sumofdigit(1798))
print(sumofdigit(178765))

