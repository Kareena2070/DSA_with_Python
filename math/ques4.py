# GCD of Two Numbers
# You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.
# he Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.

# Examples:
# Input: n1 = 4, n2 = 6
# Output: 2
# Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6
# Greatest Common divisor = 2.

# Input: n1 = 9, n2 = 8
# Output: 1
# Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.
# Greatest Common divisor = 1.


n1, n2 = map(int, input("Enter Two Numer: ").split(","))

def gcd(n1, n2):
    gcdNum = 1
    for i in range(1, min(n1, n2)):
        if n1%i ==0 and n2%i==0:
            gcdNum = i
    return gcdNum
    
print(gcd(n1,n2))