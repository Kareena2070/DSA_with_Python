# Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
# Examples:
# Input : n = 2
# Output : 1
# Explanation : F(2) = F(1) + F(0) => 1 + 0 => 1.

# Input : n = 3
# Output : 2
# Explanation : F(3) = F(2) + F(1) => 1 + 1 => 2.


n = int(input("Enter a number: "))

def fib(n):
    if n <=1:               #why we only use 1 here with <= sign only ?
        return n
    last = fib(n-1)
    sLast = fib(n-2)
    return last+sLast

print(fib(n))



def fib(n):
    if n <=1:               #why we only use 1 here with <= sign only ?
        return n
    return fib(n-1)+fib(n-2)

print(fib(n))