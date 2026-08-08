#right roation
# lst=[1,2,3,4,5]
# print(lst)
# lst=lst[-1:] + lst[:-1]
# print(lst)


#left roation

lst=[1,2,3,4,5]
lst=lst[1:] + lst[:1]
print(lst)


lst=[1,2,3,4,5]
x=lst[-1]

for i in range (len(lst)-1,0,-1):
    lst[i]=lst[i-1]
    
lst[0]=x
print(lst)
