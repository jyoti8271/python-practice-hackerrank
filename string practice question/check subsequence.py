s=str(input("enter the string"))
sub=str(input("enter the subsequence"))

j=0

for char in s:
    if j<len(sub) and char==sub[j]:
        j+=1
        
        
if j==len(sub):
    print("subsequence")
    
else:
    print('subsequence')
    