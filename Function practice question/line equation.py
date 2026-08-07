def line_equation(m,c,x):
    y=m*x+c
    return y

m=float(input("Enter the slope:"))
c=float(input("Enter the intercept :"))
x=float(input("enter the value of x:"))

result=line_equation(m,c,x)
print(result)