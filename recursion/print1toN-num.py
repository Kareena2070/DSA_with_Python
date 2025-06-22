# Print 1 to N using recursion

n = int(input("Enter a number: "))

def printNum(n):
    if n == 0:
        return
    printNum(n-1)
    print(n)


printNum(n)