# Count Odd Even Divisors
# You have an integer N, and you want to calculate the number of odd divisors of N, and the number of even divisors of N.

# For example, 2 has 1 odd divisor (which is 1), and 1 even divisor (which is 2). 8 has 1 odd divisor (which is 1) and 3 even divisors (which are 2,4,82,4,8).

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.The first and only line of input contains a single integer N.
# Output Format
# For each test case, output on a new line 2 integers - first, the number of odd divisors of N, and second, the number of even divisors of N.

# Constraints
# 1≤T≤1001≤N≤100

# Sample 1:
# Input           Output

# 5              1 0
# 1              1 1
# 2              2 0
# 3              1 2
# 4              1 3
# 8



T = int(input())
for j in range(T):
    N = int(input())
    # divisor(N)
    countE = 0
    countO = 0
    for i in range(1, N+1):
        if N%i==0:
            if i%2==0:
                countE+=1
            else:
                countO+=1
            
    print(countO, countE)
    
