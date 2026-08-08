# t=(1,2,34,5)

# if t==t[::-1]:
#     print("palindrome")
    
# else:
#     print("not palindrome")



t=tuple(map(int,input("enter the number").split()))

if t==t[::-1]:
    print("palindrome")
    
else:
    print("not palindrome")
    
    
