# Given an array, find the largest element in it.
arr = [3, 5, 7, 2, 8, -1, 4]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i] 
print("Largest element in the array is:", arr[-1])
# Time complexity = O(n^2) where n is the length of the array.
# Space complexity = O(1) as no extra space is used.



# Given a string s, return the index of the first character that does not repeat.If no such character exists, return -1.
s = "lleetcode"

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    if count == 1:
        print("Index of first non-repeating character is:", i)
        break
# Time complexity = O(n^2) where n is the length of the string.
# Space complexity = O(1) as no extra space is used.