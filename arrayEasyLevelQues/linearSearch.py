# Linear Search
# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not
# found in the array, return -1
# Examples:
# Input: nums = [2, 3, 4, 5, 3], target = 3
# Output: 1
# Explanation: The first occurence of 3 in nums is at index 1

# Input: nums = [2, -4, 4, 0, 10], target = 6
# Output: -1
# Explanation: The value 6 does not occur in the array, hence output is -1

nums = [2, 3, 4, 5, 3]
target = 8

def linearSearch(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    else:
        return "not found target in array", -1
    
print(linearSearch(nums, target))

