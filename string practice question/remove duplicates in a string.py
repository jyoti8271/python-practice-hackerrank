s=str(input("enter the string:"))

result=""

for char in s:
    if char not in result:
        result+=char
        
print(result)