# Largest Element
# Given an array of integers nums, return the value of the largest element in the array

# Examples:
# Input: nums = [3, 3, 6, 1]
# Output: 6
# Explanation: The largest element in array is 6

# Input: nums = [3, 3, 0, 99, -40]
# Output: 99
# Explanation: The largest element in array is 99


# brute force
# arr = [3, 3, 6, 1]
arr = [1, 2, 3, 4, 5]
n = len(arr)
for num in range(n-1):
    min = num
    for el in range(num, n):
        if arr[el] < arr[min]:
            min = el
    arr[num], arr[min] = arr[min], arr[num]
arrs = arr
print("Largest element in an array",arrs[n-1])

# Time Complexity 
# outer loop runs for (n-1) and inner loop runs for (n) so Time Complexity is O(n^2)


# Optimal force
# nums = [3, 3, 0, 99, -40]
nums = [1, 2, 3, 4, 5]
largest = nums[0]
n = len(nums)
for i in range(n):
    if nums[i]>largest:
        largest = nums[i]

print("Largest Number in an array: ", largest)

# Time complexity
# only one loop runs n times of Time complexity is O(n)