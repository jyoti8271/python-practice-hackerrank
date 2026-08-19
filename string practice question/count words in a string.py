s=str(input("enter the string:"))
word=s.split()

total=len(word)
print(total)




#count the letter of words:
s=str(input("enter the string"))
count=0

for char in s:
    if char.isalpha():
        count+=1
    
print(count)
    