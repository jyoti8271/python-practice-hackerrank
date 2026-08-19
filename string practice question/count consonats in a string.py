# s=input("enter string:")

# count=0

# for char in s:
#     if char.isalpha():
#         if char not in "aeiouAEIOU":
#             count+=1
            
# print(count)





s=input("enter the string:")

vowels=0

for char in s:
    if char in "aeiouAEIOU":
        vowels+=1
        
consonants=len(s)-vowels
print(consonants)
