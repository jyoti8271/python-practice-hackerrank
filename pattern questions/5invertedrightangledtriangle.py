# n=int(input("enter the number"))

# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()


def right(n):
    result=[]
    for i in range(n,0,-1):
        result.append("*" *i)
        
    return result

n=int(input("enter the number"))

rows=right(n)
for row in rows:
    print(row)