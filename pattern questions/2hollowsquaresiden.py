
# n=int(input("enter the numbers"))

# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")    
            
#     print()
       
    
    
def hollw(n):
    result=[]
    for i in range (n):
        if i==0 or i==n-1:
            result.append("*" *n)
        
        else:
            result.append("*" +" "*(n-2)+"*")
            
    return result

n=int(input())
rows=hollw(n)

for star in rows:
    print(star)