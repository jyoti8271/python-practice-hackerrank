def power(n):
    #base case
    if n==1:
        return 2
    
    smallans=power(n-1)
    ans=2*smallans
    return ans

print(power(8))