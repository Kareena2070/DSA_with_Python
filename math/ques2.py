# Reverse a number
# You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
# Examples:
# Input: n = 25
# Output: 52
# Explanation: Reverse of 25 is 52.

# Input: n = 123
# Output: 321
# Explanation: Reverse of 123 is 321.

n = int(input("Enter number"))

def revserseNum(n):                                     #54             
    reversedNum = 0                                     #0
    while n>0:                                          #54 >0              5 > 0           0 > 0   stop
        lastNum = n%10                                  #54%10 = 4          5%10 = 5
        reversedNum = reversedNum*10+lastNum            #0*10+4 = 4         4*10+5 = 45
        n = n//10                                       #54//10 = 5         0//10 = 0
    return reversedNum                                                                      #45

print(revserseNum(n))