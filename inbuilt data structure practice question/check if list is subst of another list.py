# list1=[1,2,3]
# list2=[1,2,3,4,5]


# if set(list1).issubset(set(list2)):
#     print("list 1 is subset of list2")
    
# else:
#     print("list 1 is not a subset of list2")



lst1=list(map(int,input("enter first elements").split()))
print(lst1)


lst2=list(map(int,input("enter second elements").split()))

print(lst2)

if set(lst1).issubset(set(lst2)):
    print("list 1 is subset of list2")
    
else:
    print("list 1 is not a subset of list2")




    