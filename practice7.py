# 7. Prime Number Checker: Check whether a given number is prime using a for loop.

number = int(input("Enter your number: "))

# def primeNum(number):
#     for i in range(2, number):
#         if number%i==0:
#             print( number,"not prime")
#             return
#     print(number, "prime")       

# primeNum(number)


def primeNumber(number):
    count = 0
    for i in range(2, number):   # here 1 and num itself is not include so if condition get true 1 time count will increase
        if number%i==0:
            count+=1
    if count==0:
            print("prime")
    else:
            print("not prime")

primeNumber(number)


