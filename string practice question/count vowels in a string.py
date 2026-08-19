# s=str(input("enter the string"))

# count=0

# for char in s:
#     if char in "aeiouAEIOU":
#         count+=1
# print(count)






s=str(input("enter the string"))
vowel=0
for char in s:
    if char in "aeiouAEIOU":
        vowel+=s.count(char)
        
print(vowel)