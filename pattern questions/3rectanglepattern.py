# n=int(input("enter the numbers of rows:"))
# m=int(input("enter the number of columns"))

# for i in range(n):
#     for j in range(m):
#         print("*",end=" ")
#     print()
    
    
    
def rect(n,m):
    result=[]
    for i in range(n):
        result.append("*" *m)
    return result

n=int(input())
m=int(input())

rectangel=rect(n,m)
for react in rectangel:
    print(react)
        