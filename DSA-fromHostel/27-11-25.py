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




# 3. Bubble Sort Question
# Q:Given an array of integers, sort the array in ascending order using Bubble Sort.
# Example
# Input:
# [5, 2, 9, 1, 5, 6]
# Output:
# [1, 2, 5, 5, 6, 9]

arr = [5, 2, 9, 1, 5, 6]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print("Sorted arr: ", arr)