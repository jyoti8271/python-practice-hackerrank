# n=int(input())

# for i in range(n):
#     for j in range(n):
#         print(f"*",end="")
#     print()



def square(n):
    result=[]
    
    for i in range(n):
        result.append("*" *n)
    return result
n=int(input())
rows=square(n)


for row in rows:
    print(row)
