
def number_of_rouds_lift(total,capacity):
    rounds=(total+capacity-1)//capacity
    return rounds

total=int(input("enter the total:"))
capacity=int(input("enter the capacity:"))

result=number_of_rouds_lift(total,capacity)
print(f"{result}")
    