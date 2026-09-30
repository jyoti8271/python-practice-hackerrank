import sys
sys.setrecursionlimit(5000)

def sumofN(n):
    #base case
    if n==1:
        return 1
    
    smallans= sumofN(n-1)
    ans=n+smallans
    
    return ans

print(sumofN(10))