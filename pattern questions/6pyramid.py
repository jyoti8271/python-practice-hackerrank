# n=int(input("enter the number"))
# for i in range(n):
#     #spaces
#     for j in range(n-1-i):
#         print(" ",end="")
        
#     #stars
#     for k in range(2*i+1):
#         print("*", end="")
        
#     print()
    
    
        
# def pyramid(n):
#     result=[]
    
#     for i in range(n):
#         space=" " * (n-i-1)
#         star="*" * (2*i+1)
#         result.append(space+star)
#     return result

# n=int(input("enter the number"))
# rows=pyramid(n)
# for row in rows:
    # print(row)
    
    
    
    n = int(input())

for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))