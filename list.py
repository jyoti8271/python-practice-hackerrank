# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Example






# : Append  to the list, .
# : Append  to the list, .
# : Insert  at index , .
# : Print the array.
# Output:
# [1, 3, 2]
# Input Format

# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

# Sample Input 0

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
# Language
# Pypy 3
# More
# 123456789101112131415161718192021222324
# if __name__ == '__main__':
#     n = int(input())
#     lst = []

#     for i in range(n):
#         command = input().split()

#         if command[0] == 'insert':
#             lst.insert(int(command[1]), int(command[2]))

# …            lst.sort()

#         elif command[0] == 'pop':
#             lst.pop()

#         elif command[0] == 'reverse':
#             lst.reverse()
# Line: 27 Col: 26

# Test against custom input
# Python
# You have earned 10.00 points!
# You are now 95 points away from the 4th star for your python badge.
# 14%125/220
# Congratulations
# You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn

# Test case 0

# Test case 1
# Compiler Message
# Success
# Input (stdin)
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Expected Output
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]




















if __name__ == '__main__':
    n = int(input())
    lst = []

    for i in range(n):
        command = input().split()

        if command[0] == 'insert':
            lst.insert(int(command[1]), int(command[2]))

        elif command[0] == 'print':
            print(lst)

        elif command[0] == 'remove':
            lst.remove(int(command[1]))

        elif command[0] == 'append':
            lst.append(int(command[1]))

        elif command[0] == 'sort':
            lst.sort()

        elif command[0] == 'pop':
            lst.pop()

        elif command[0] == 'reverse':
            lst.reverse()