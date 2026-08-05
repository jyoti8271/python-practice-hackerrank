# n=int(input("enter the number"))
# for i in range (1,n+1): #rows
#     for j in range(i): #stars
#          print("*",end=" ")
         
#     print()
     
     
     
# def right(n):
#     result=[]
#     for i in range (1,n+1):
#         row=" "   #har bar row empty se start hogi
        
#     for j in range(i):
#         row+="*"
        
#     result.append(row)
    
#     return result

# n=int(input("enter the number"))
# rows=right(n)

# for row in rows:
#     print(row)


def right(n):
    for i in range(1,n+1):
        
        for j in range(i):
            print("*",end=" ")
        
        print()
        
n=int(input("enter the number"))

right(n)


         
        