# Expensive Buying
# Chef is in a shop with N distinct items. The ii-th item is sold at a price of Ci.

# Chef only wants expensive items, and so he has decided that he will buy the K most expensive items. Find how much total cost Chef had to pay to buy the K most expensive items.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of multiple lines of input.
# The first line of each test case contains 2 integers - N and K.
# The second line contains NN integers - C1,C2,​…,C N.

# Output Format
# For each test case, output on a new line the total cost to buy K most expensive items.


T = int(input("test case"))
for i in range(T):
    n, k = list(map(int, input("Number of items sell and  can sell").split()))
    c = list(map(int, input("perices").split()))
    sumNum = 0
    if n<k:
        print(0)
    c.sort()

    y = n-k-1
    if n >=k:
        for i in range(len(c)-1,y,-1):
            sumNum+=c[i]
    print(sumNum)