# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Example




# The query_name is 'beta'. beta's average score is .

# Input Format

# The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

# Constraints

# Output Format

# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

# Sample Input 0

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output 0

# 56.00
# Explanation 0

# Marks for Malika are  whose average is 

# Sample Input 1

# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh
# Sample Output 1

# 26.50
# Language
# Pypy 3
# More
# 12345678910111213141516171819
# n=int(input())
# student_marks={}

# for i in range(n):
#     data=input().split()
    
#     name=data[0]

#     marks=list(float(data[1:]))

#     student_marks[name]=marks
    
#     #query name
# query_name=input()

# marks=student_marks[query_name]
# average=sum(marks)/len(marks)
# print("{:.2f}".format(average))

# Line: 1 Col: 1

# Test against custom input
# Runtime Error :(

# Ask your friends for help:Share on FacebookShare on TwitterShare on LinkedIn

# Test case 0

# Test case 1

# Test case 2

# Test case 3

# Test case 4

# Test case 5

# Test case 6

# Test case 7

# Test case 8
# Compiler Message
# Runtime Error
# Input (stdin)
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Expected Output
# 56.00
# BlogScoringEnvironment


n = int(input())
student_marks = {}

for i in range(n):
    data = input().split()

    name = data[0]
    marks = list(map(float, data[1:]))

    student_marks[name] = marks

# query name
query_name = input()

marks = student_marks[query_name]
average = sum(marks) / len(marks)

print("{:.2f}".format(average))




########by for loop
n=int(input())

names=[]
marks=[]

for i in range(n):
    data=input().split()
    
    names.append(data[0])
    marks.append(list(map(float,data[1:])))
    
query=input()
    
for i in range(n):
    if names[i]==query:
            
        average=sum(marks[i])/len(marks[i])
            
        print("{:.2f}".format(average))
