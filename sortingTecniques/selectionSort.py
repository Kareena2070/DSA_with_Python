# Selection Sort
# Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and return the sorted array.

# A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.
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
for i in range(n-1):
    min = i
    for j in range(i, n):
        if nums[j]<nums[min]:
            min = j
    nums[i], nums[min] = nums[min], nums[i]
print(nums)

# Time Complexity
# Outer loop runs n-1 time 
# inner loop runs n time 
# total time complexity is 0(n^2)


# Important Notes:
# Best Case Time Complexity: O(n²)
# Even if the array is already sorted, Selection Sort still does all comparisons.

# Worst Case Time Complexity: O(n²)

# Space Complexity: O(1) → In-place sorting, no extra space used.