# 2089. Find Target Indices After Sorting Array
# level: Easy
# You are given a 0-indexed integer array nums and a target element target.
# A target index is an index i such that nums[i] == target.
# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.
# Example 2:

# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.
# Example 3:

# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.
 
nums = [1,2,5,2,3]
target = 2

nums = [1,2,5,2,3]
target = 5

def targetIndices( nums, target):
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i]>nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        sortNum = nums
        arr = []
        for l in range(len(sortNum)):
            if sortNum[l] == target:
                arr.append(l)
        return arr

print(targetIndices(nums, target))
# Output: [1, 2]
# Time complexity: O(n^2) due to the nested loops for sorting.
# Space complexity: O(1) as no extra space is used except for the output list