# 2. Max of Three Numbers: Write a function that takes three numbers as input and returns the largest using conditional statements.

a, b, c= map(int, input("Enter any three number:").split())

def maxNum(a, b, c):
    if a > b:
        if a > c:
            print("largest number:", a)
        elif c > b:
            print("largest number: ", c)
        else:
            print("largest number: ", b)
    else:
        print("largest number: ", b)

maxNum(a, b, c)