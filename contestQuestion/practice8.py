# Alternate Jumps
# There are N lily pads, arranged in a line. They are numbered 1 to N from left to right.

# A frog is initially standing on lily pad N. The frog loves to jump, so it will perform a sequence of (N−1) jumps with alternating directions as follows:

# First, jump to the lily pad N−1 positions to the left of its current position.Next, jump to the lily pad N−2 positions to the right of its current position.Next, jump to the lily pad N−3N−3 positions to the left of its current position.⋮More formally, in the i-th jump (1≤i≤N−1(1≤i≤N−1),

# If i is odd, the frog will jump to the lily pad N−i positions to the left of its current position.That is, if its current position is X, its new position will be X−(N−i)X−(N−i).If i is even, the frog will jump to the lily pad N−i positions to the right of its current position.That is, if its current position is X, its new position will be X+(N−i)X+(N−i).
# It can be proved that all of the frog's jumps are valid - that is, it will always be on one of the lily pads 1 to N.
# You're given N. Can you find the number of the final lily pad the frog will end up at?

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.Each test case consists of a single line of input, containing a single integer N.
# Output Format
# For each test case, output on a new line the answer: the final position of the frog.

# Sample 1:
# Input = 3
# 2
# 3
# 4
# Output = 1
# 2 
# 3
# T = 3
# N = [2, 3, 4]
T = int(input("enter the number of test cases: "))
for _ in range(T):
    N = int(input())
    if N % 2 == 0:
        print(N // 2)
    else:
        print((N // 2) + 1)
