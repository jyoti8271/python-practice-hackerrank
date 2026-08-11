binary=int(input("enter the number"))

decimal=int(binary,2)

print("decimal =",decimal)








binary=input("enter the binary number:")

decimal=0

for digit in binary:
    decimal=decimal * 2+int(digit)
    
    
print("decimal =", decimal)





n=int(input("enter the number:"))

binary=""


for i in range(10):
    remainder= n%2
    
    binary =str(remainder) +binary
    n=n//2
    
    if n==0:
        break
    
print(binary)








