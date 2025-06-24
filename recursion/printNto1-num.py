# Print N to 1 using recursion

n = int(input("Enter a number: "))

def printNum(n):
    if n ==0:
        return
    print(n)
    printNum(n-1)

printNum(n)