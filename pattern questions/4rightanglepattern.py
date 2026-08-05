# n=int(input("enter the number n:"))

# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()    


def right(n):
    result=[]
    
    for i in range(n):
        result.append("*" *i)
    return result

n=int(input("enter the number"))
rows=right(n)
for row in rows:
    print(row)