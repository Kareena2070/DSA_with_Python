# Playing with Toys
# Chef got N toys for his birthday. Everyday, if he has at least one toy with him, he plays with one specific toy for that day.

# Unfortunately, Chef is very careless, and will inevitably break that toy by the end of the day. When he does break it, he does not play with a new toy but just waits for the next day.

# After M days, how many toys will Chef be left with?

# Example usage:
# Input:
# 5 2
# Output:
# 3

n,m = list(map(int, input("number toys and number of days: ").split()))

k = n-m
if k < 0:
    print(0)
else:
    print(k)


# Add to make Positive
# An array A of length N is called good if the sum of all it's elements is non-negative, i.e. (A1+A2+…+AN)≥0(A 1​+A 2​+…+A N​)≥0.

# Find the minimum non-negative integer X such that if you add X to each element of the array, the array becomes good. That is, an array B of length N, defined as Bi=Ai+XB i​=A i +X, is good.

import math
t = int(input("Number of test cases: "))

for _ in range(t):
    n = int(input("Array length: "))
    a = list(map(int, input("array list: ").split()))
    
    x = sum(a)
    
    if x >= 0:
        print(0)
        
    else:
        y = math.ceil((-x)/n)
        print(y)


