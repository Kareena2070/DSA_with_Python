# Signal
# A secret binary transmission is represented by a string S of length N.

# In this signal:
# 0 represents a silence period.
# 1 represents a pulse period.

# Your task is to determine how many pulses occurred after at least one silence had already appeared in the transmission.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of two lines:
# The first line contains an integer N — the length of the binary string.
# The second line contains the binary string S.

# Output Format
# For each test case, output on a new line the number of pulses occurred after at least one silence had already appeared in the transmission.

# t = 2
# n = 3  n = 011
# n = 3  n = 101

t = int(input("Number of test case: "))

for _ in range(t):
    n = int(input( "length of binary string: "))
    s = input("enter binary string: ")
    count = 0
    for i in range(n-1, -1, -1):
        if s[i] == "1":
            count = count+1
        else:
            break
    if count == n:
        print(0)
    
    print(count)
            
