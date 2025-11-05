# Buying Chairs
# Chef is redecorating his house, and is now trying to decide which chairs to buy.

# The furniture store Chef is visiting has W wooden chairs and P plastic chairs available.
# Chef believes that each wooden chair will increase the stylishness of his house by 2, while each plastic chair will increase the stylishness of his house by 1.

# Chef wants to buy exactly K chairs in total.
# It is guaranteed that K≤W+P.

# Find the maximum possible stylishness Chef can attain by purchasing exactly K chairs from the store.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# The first and only line of each test case contains three space-separated integers 
# W,P, and K — the number of wooden chairs available, the number of plastic chairs available, and the total number of chairs Chef wants to buy.
# Output Format
# For each test case, output on a new line the answer: the maximum possible stylishness Chef can attain by buying K chairs.

# smaple 1:
# Input
# 3
# 4 3 5
# 2 5 4
# 6 1 6
# Output
# 9
# Explanation
# Test case 1: Chef can buy 4 wooden chairs and 1 plastic chair, attaining a stylishness of 2⋅4+1⋅1=9.    

t = int(input("number of test case: "))

for _ in range(t):
    w, p, k = list(map(int, input("wooden chair, plastic chair, total chair chef buy: ").split()))
    if w < k:
        i = k-w
        print((w*2)+(i*1))
    elif w >=k:
        print(k*2)