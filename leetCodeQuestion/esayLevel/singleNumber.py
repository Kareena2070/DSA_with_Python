# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1



# brute force approach
from collections import Counter
def singleNumber(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count +=1
        if count == 1:
            return nums[i]
nums = [4,1,2,1,2]
singleNumber(nums)

# Time Complexity
# Outer loop: → O(n)
# Inner loop: → O(n) per iteration
# Total: O(n × n) = O(n²)
                    
# Space Complexity
# Only a few integer variables (i, j, count) are used.
# O(1) space




# better approach
def singleNumber(nums):
    feaq = Counter(nums)
    for num, count in feaq.items():
        if count == 1:
            print(num)

nums = [2,2,1]
singleNumber(nums)

# Time Complexity
# Counter(nums) → O(n), because it iterates through all n elements to count frequencies.
# for num, count in feaq.items() → O(k), where k is the number of unique elements. In worst case, k = n.
# Overall: O(n)

# Space Complexity
# Counter(nums) stores counts of unique elements → O(k), worst case O(n).
# feaq.items() iteration uses negligible extra space.
# Overall: O(n)


        
