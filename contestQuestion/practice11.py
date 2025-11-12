
# Basketball Score
# A basketball team scored X successful 3-pointers and Y successful 2-pointers in a game.
# Your task is to compute the total score of the team.

# Each 3-pointer is worth 3 points, and each 2-pointer is worth 2 points.

# Input Format
# A single line containing two integers X and Y — the number of successful 3-pointers and 2-pointers respectively.

# Output Format
# Print a single integer — the total score of the team.

# example 1:
# input  = 2, 3
# output = 12
# example 2:
# input = 1, 3
# output = 9

x,y = list(map(int, input("enter x and y: ").split()))

print((x*3)+(y*2))
