# # lst=[1,2,3,4,5]

# # if len(lst)==len(set(lst)):
# #     print("all values are unique")
    
# # else:
# #     print("duplicates")


# user se input

lst=list(map(int,input("enter elements:").split()))

if len(lst)==len(set(lst)):
    print("all elemnts are unique")
    
else:
    print("duplicate elements are found")