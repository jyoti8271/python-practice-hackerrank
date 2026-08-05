# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

# Example




# All permutations of  are:
# .

# Print an array of the elements that do not sum to .


# Input Format

# Four integers  and , each on a separate line.

# Constraints

# Print the list in lexicographic increasing order.

# Sample Input 0

# 1
# 1
# 1
# 2
# Sample Output 0

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Explanation 0

# Each variable  and  will have values of  or . All permutations of lists in the form .
# Remove all arrays that sum to  to leave only the valid permutations.

# Sample Input 1

# 2
# 2
# 2
# 2
# Sample Output 1

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
# Language
# Pypy 3
# More
# 12345678910111213
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
    
#     result=[[i,j,k]
#         for i in range(x + 1)
#         for j in range (y + 1)
#         for k in range(z + 1)

# Line: 10 Col: 25

# Test against custom input
# Congratulations!

# You have passed the sample test cases. Click the submit button to run your code against all the test cases.


# Sample Test case 0

# Sample Test case 1
# Input (stdin)
# 1
# 1
# 1
# 2
# Your Output (stdout)
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Expected Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

x=int(input())
y=int(input())
z=int(input())
n=int(input())

result=[[i,j,k]
        for i in range(x+1)
        for j in range(y+1)
        for k in range(z+1)
        if i+j+k!=n]


print(result)