# 9. Reverse a String: Write a program to reverse a string using a loop.

name = input("Enter you full name: ")

for i in range(1, len(name)+1):
    reverseStr = name[-i]
    print(reverseStr, end="")
print()


