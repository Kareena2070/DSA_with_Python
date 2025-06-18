# Divide into 3

# You have N  toffees and 3 friends. You will divide the toffees among your friends (You are too generous to take one yourself).
# You want to make sure that your division is fair. Hence, you want to minimize the imbalance of your division.
# Here, the imbalance is defined as (mx−mn)(mx−mn), where mx is the maximum toffees any friend received, and mn is the minimum toffees any friend received.
# For example, if the you give 3,1,43,1,4 toffees to your friends, then mx=4mx=4 and mn=1mn=1, so the imbalance is 4−1=34−1=3.
# Find the minimum possible imbalance.
# Input Format
# The first and only line of input contains a single integer N - the number of toffees you had.
# Output Format
# For each test case, output on a new line the minimum possible imbalance.

# Constraints
# 3≤N≤10
# 3≤N≤10

# Sample 1:
# Input       3
# Output      0


# Sample 2:
# Input     8
# Output    1


# cook your dish here
N = int(input())
num = N%3

if num==0:
    print(0)
elif num - 3:
    if 2:
        print(1)