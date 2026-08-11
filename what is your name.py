# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.

# Function Description

# Complete the print_full_name function in the editor below.

# print_full_name has the following parameters:

# string first: the first name
# string last: the last name
# Prints

# string: 'Hello  ! You just delved into python' where  and  are replaced with  and .
# Input Format

# The first line contains the first name, and the second line contains the last name.

# Constraints

# The length of the first and last names are each ≤ .

# Sample Input 0

# Ross
# Taylor
# Sample Output 0

# Hello Ross Taylor! You just delved into python.
# Explanation 0

# The input read by the program is stored as a string data type. A string is a collection of characters.

# Language
# Pypy 3
# More
# 12345678910111213141516
# def print_full_name(first,last):
#     print(f"Hello {first} {last}! You just delved into python.")


# # The function is expected to return a STRING.
# # The function accepts following parameters:
# #  1. STRING first
# #  2. STRING last
# #


# Line: 2 Col: 27

# Test against custom input
# Congratulations!

# You have passed the sample test cases. Click the submit button to run your code against all the test cases.


# Sample Test case 0
# Input (stdin)
# Ross
# Taylor
# Your Output (stdout)
# Hello Ross Taylor! You just delved into python.
# Expected Output
# Hello Ross Taylor! You just delved into python.



def print_full_name(first,last):
    print(f"Hello {first} {last}! You just delved into python.")


# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#



if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
