# n=int(input("enter the number"))

# for i in range(n):
    
#     #space print
#     for j in range(i):
#         print(" ",end="")
    
#     #star print
        
#     for k in range(2 *(n-i)-1):
#         print("*",end="")
# print()
        
        
        
        

    
    
    
def invert(n):
    result=[]
    
    for i in range(n):
        spaces=" " * i
        stars="*" * (2*(n-i)-1)
        result.append(spaces+stars)
    return result

n=int(input("enter the numbers"))

rows=invert(n)
for row in rows:
    print(row)
