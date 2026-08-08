#sum of two consecutive by simple and for loop

# lst=[1,2,3,4,5]

# for i in range (len(lst)-1):
#     print(lst[i] + lst[i+1])
    
    
    
    
    
    
# lst=[1,2,3,4,5]
# max=0

# for i in range(len(lst)-1):
#     total=lst[i]+lst[i+1]
    
#     if total > max:
#         max=total
        
# print(max)




#differnce of two consecutive elements

lst=[1,2,3,4,56]

max=0

for i in range(len(lst)-1):
    difference=abs(lst[i+1]-lst[i])
    
    print(lst)
    
    if difference>max:
        max=difference
        
print(max)

    
    