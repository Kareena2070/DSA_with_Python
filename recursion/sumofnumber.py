# Sum of first N numbers

n = int(input("Enter a number: "))

def sumNum(n):
    if n == 1:
        return 1
    return n + sumNum(n-1)

print(sumNum(n))