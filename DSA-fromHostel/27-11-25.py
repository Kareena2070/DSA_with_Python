# 3. Count even numbers in an array
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

