# 169. Majority Element
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

nums = [2,2,1,1,1,2,2]
from collections import Counter

def MajorityElement(nums):
    freq = Counter(nums)
    n = len(nums)
    for i in range(n):
        if freq[nums[i]]>n//2:
            return nums[i]

print(MajorityElement(nums))


# Time complexity = O(n)
# space complexity = O(n) -- because Counter(nums) creates a dictionary that stores the frequency of each unique element.