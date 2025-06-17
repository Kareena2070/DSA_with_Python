# Count all Digits of a Number
# You are given an integer n. You need to return the number of digits in the number.

# The number will have no leading zeroes, except when the number is 0 itself.

# Examples:
    # Input: n = 4
    # Output: 1
    # Explanation: There is only 1 digit in 4.

    # Input: n = 14
    # Output: 2
    # Explanation: There are 2 digits in 14.


def countDigit(n):
    count = 0
    if n <=0:
        return 1

    while n>0:
        lastDigit = n%10
        count+=1
        n = n//10
    return count

print(countDigit(1234))
print(countDigit(4))
print(countDigit(0))