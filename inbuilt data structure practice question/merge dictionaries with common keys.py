d1={'a':30,'b':20}
d2={'a':70,'b':90}

d=d1.copy()
print(d)

for key in d2:
    if key in d:
        d[key] += d2[key]
        
    else:
        d[key]=d2[key]
        
print(d)