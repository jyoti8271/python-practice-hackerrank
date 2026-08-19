s=str(input("enter the string"))
words=s.split()
longest=""

for word in words:
    if len(word)>=len(longest):
        longest=word
        
print(longest)
print(len(longest))
        
        