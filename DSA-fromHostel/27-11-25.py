# 1. Count even numbers in an array
# Input: [2, 5, 6, 7, 8]
# Output: 3

arr = [2, 5, 6, 7, 8]
count = 0

for i in range(len(arr)):
    if arr[i]%2 == 0:
        count+=1
print("Count of even numbers in an array: ", count)
# Time complexity = O(n) where n is the length of the array.
# Space complexity = O(1) as no extra space is used.




# 2. Count occurrences of a character
# Input: string = "banana", char = "a"
# Output: 3

string = "bananaaa"
char = "a"
count = 0
for i in range(len(string)):
    if string[i] == char:
        count+=1
print("Char count occurrences in a string: ", count)



