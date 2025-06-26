# Factorial of N numbers

n = int(input("Enter a number: "))

def factorialNum(n):
    if n == 0:
        return 1
    return n*factorialNum(n-1)

print(factorialNum(n))