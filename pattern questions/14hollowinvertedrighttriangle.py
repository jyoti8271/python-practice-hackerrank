# n=int(input())

# for i in range(n,0,-1):
#     for j in range(i):
#         if j ==0 or j==i-1 or i==n:
#             print("*", end="")
            
#         else:
#             print(" ",end="")
#     print()
    
    
def hollow_inverted_triangle(n):
    for i in range (n,0,-1):
        for j in range (i):
            if j==0 or j==i-1 or i==n:
                print("*",end="")
            else:
                print(" ",end="")
                
        print()

n=int(input())
hollow_inverted_triangle(n)
    