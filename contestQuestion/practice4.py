# Triangles
# It is well known fact in mathematics that the sum of the 3 angles in a triangle is 180 degrees.

# You had a triangle, but unfortunately you only remember the 1st and 2nd angles of it, and you have forgotten the 3rd one.

# Given that the first angle was A, and the second was B, can you figure out the third one? All angles are integers measured in degrees.

# Input Format
# The first and only line of input contains 2 integers - A and B.

# Output Format
# Print a single integer - the measure of the 3rd   angle (in degrees).

# Constraints
# 1≤A,B<180
# A+B<180

# Sample 1:
# Input: 60 60 
# Output: 60
# Input: 1 1
# output: 178

a, b = list(map(int, input("Two side of Triangles: ").split()))

print("Third side will be: ",180-(a+b))

