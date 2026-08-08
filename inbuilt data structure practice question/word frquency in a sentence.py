sentence="hello world hello pyhton hello python hello wolrd hello jii"

words=sentence.spilt()

freq={}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] =1
        
print(freq)




# #throght set
# sentence="cat dog cat aplle cat"
# words=sentence.spilt()

# for word in set(words):
#     print(word,words.count(word))



sentence="cat dog cat dog camel heri born "
freq=[]

for word in words:
    if word not in freq:
        freq.append(word)
        
for word in freq:
    print(word,words.count(word))
    
     

    