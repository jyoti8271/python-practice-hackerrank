# n=int(input())
# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()



def pyramid(n):
    for i in range (1,n+1):
        for j in range(1,i+1):
            print(j, end="")
        print()
        
n=int(input())
pyramid(n)