# Check for Prime Number
# You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.
# A prime number is a number which has no divisors except 1 and itself.
# Examples:
# Input: n = 5
# Output: true
# Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

# Input: n = 8
# Output: false
# Explanation: The divisors of 8 are 1, 2, 4, 8, thus it is not a prime number.


n = int(input("Enter your number: "))

def primeNum(m):
    count = 0
    for i in range(1, m):
        if m%i==0:
            count +=1
    if count ==1:
        return True
    else:
        return False
print(primeNum(n))