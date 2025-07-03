# Insertion Sorting
# Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.
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
for i in range(n):
    temp = nums[i]
    j = i-1
    while j >=0 and nums[j]>temp:
        nums[j+1] = nums[j]
        j-=1
    nums[j+1] = temp
print(nums)