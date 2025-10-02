# Remaining Money
# Chef had N rupees with him.
# He decided to buy 
# Aice creams for his friends, each at a cost of  rupees. He was able to pay the entire amount.

# Find how many rupees Chef still has left with him at the end?
# nput Format
# The first and only line of input contains 3 integers - N,A and nB.
# Output Format
# For each test case, output on a new line the amount of rupees Chef has left.
# Sample 1:
# input = 100, 5, 2
# output = 90

# smaple2:
# input = 10, 5, 2
# output = 0

n, a, b = list(map(int, input().split()))

print(n - (a*b))