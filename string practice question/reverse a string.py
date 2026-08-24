# s=str(input("enter the string"))
# reverse=s[: : -1]
# print(reverse)


s=str(input("enter the string"))
reverse=""
for i in range(len(s)-1, -1, -1):
    reverse += s[i]
    
print(reverse)