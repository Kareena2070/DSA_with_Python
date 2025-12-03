# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


# brute force 
nums = [2,3,4]
target = 6

def twoSum(nums, target):
    arr = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                arr.append(i)
                arr.append(j)
    return arr

print(twoSum(nums, target))


# time complexity = O(n^2)
# two loop runs
# Space Complexity = O(1)



# better approach
def twoSum(nums, target):
    freq = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in freq:
            return [freq[complement], i]
        freq[num] = i
print(twoSum(nums, target))

# Time complexity = O(n)
# Soace complxity = O(n)  -- because dic(num_count sortes n number)

# revision
def twoSum(nums, target):
    num ={}
    for i in range(len(nums)):
        nextNum = target - nums[i]
        if nextNum in num:
            return [num[nextNum], nums[i]]
        
        num[nums[i]] = i

print(twoSum([20, 8, 2, 8, 10], 10))
