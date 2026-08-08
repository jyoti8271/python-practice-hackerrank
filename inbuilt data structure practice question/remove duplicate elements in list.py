# lst=[1,2,3,4,5,5]

# new=[]

# for i in lst:
#     if i not in new:
#         new.append(i)
        
# print(new)







lst=[1,2,3,3,4,5]
new=list(set(lst))
print(new)




lst=[1,2,3,4,3,4,3,]
new=[]

[new.append(i) for i in lst if i not in new]

print(new)




