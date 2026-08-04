# Check Tutorial tab to know how to to solve.

# The included code stub will read an integer, , from STDIN.

# Without using any string methods, try to print the following:


# Note that "" represents the consecutive values in between.

# Example

# Print the string .

# Input Format

# The first line contains an integer .

# Constraints


# Output Format

# Print the list of integers from  through  as a string, without spaces.

# Sample Input 0

# 3
# Sample Output 0

# 123

def is_leap(year):
    leap=False

    if year%400==0:
        leap=True
        
    elif year%100==0:
        leap=False
        
    elif year%4==0:
        leap=True
        
    return leap

year=int(input())
print(is_leap(year))