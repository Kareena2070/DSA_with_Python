# 6. Sum of Digits: Write a program to find the sum of the digits of an integer using a while loop.
number = int(input("Enter you number: "))

def sumDigit(number):
    i=1
    sum = 0
    while i <= number:
        sum +=i
        i+=1
    print(sum)

sumDigit(number)
