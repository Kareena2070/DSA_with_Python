# 13. Squares of Even Numbers: Given a list of numbers, use list comprehension to generate a new list containing squares of only even number

num = int(input("Enter a number: "))
evenNum = []
for i in range(1, num+1):
    if i%2==0:
        evenNum.append(i)
print("",evenNum)
squareEven = [i**2 for i in range(1, num+1) if i%2==0 ]
print("Square number of Even number: ", squareEven)