# Bubble Sort
# Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.
# A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
# Examples:
# Input: nums = [7, 4, 1, 5, 3]
# Output: [1, 3, 4, 5, 7]
# Explanation: 1 <= 3 <= 4 <= 5 <= 7.
# Thus the array is sorted in non-decreasing order.

# Input: nums = [5, 4, 4, 1, 1]
# Output: [1, 1, 4, 4, 5]
# Explanation: 1 <= 1 <= 4 <= 4 <= 5.
# Thus the array is sorted in non-decreasing order.

nums = [7, 4, 1, 5, 3]
n = len(nums)
for i in range(n, 1, -1):
    for j in range(i-1):
        if nums[j]> nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)


# Time complexity 
# outer loop runs n to 1 so O(n-1)
# inner loop till i-1 basic n 
# Total time complexity is O(n^2) in all cases
#  Space Complexity: O(1)