# d1={'a':10,'b':30}
# d2={'c':20,'d':30}
# d3={'e':20,'f':90}

# d={}

# d.update(d1)
# d.update(d2)
# d.update(d3)

# print(d)\
    
    
d1={'a':10,'b':30}
d2={'c':20,'d':30}
d3={'e':20,'f':90}

d={}

for dic in [d1,d2,d3]:
    for key in dic:
        if key in d:
            d[key]+=dic[key]
            
        else:
            d[key]=dic[key]
            
print (d)



