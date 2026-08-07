def  celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    
    return fahrenheit

celsius=float(input("enter the celsius"))
result=celsius_to_fahrenheit(celsius)
print(f"{result}") 