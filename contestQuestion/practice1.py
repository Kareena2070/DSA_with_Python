# Rectangle and Square
# You have a rectangle of length A units and breadth B units. You also have a square with side length of C units.

# Check if both the rectangle and the square have the same area. Print Yes if they have the same area, and No otherwise.

# Input Format:
# The first and only line of input contains 3 integers - A, B and C.
# Output Format:
# Output on a new line Yes if they have the same area, and No otherwise.

# Constraints = 1≤A,B,C≤10

# Sample 1:
# Input  = 2 8 4
# Output = Yes

# Sample 2:
# Input = 3 5 4
# Output = No


A, B, C = map(int, input().split())

rect = A *B 
squa = C * C 

if rect == squa:
    print("Yes")
else:
    print("No")

