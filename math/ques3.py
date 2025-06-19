# Palindrome Number
# You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.
# A palindrome number is a number which reads the same both left to right and right to left.
# Examples:
# Input: n = 121
# Output: true
# Explanation: When read from left to right : 121.
# When read from right to left : 121.

# Input: n = 123
# Output: false
# Explanation: When read from left to right : 123.
# When read from right to left : 321.

n = int(input())

def palindrome(n):
    num = 0
    original = n
    while n>0:
        lastNum = n%10
        num = num*10+lastNum
        n = n//10
    if num == original:
        return True
    else:
        return False
    
print(palindrome(n))