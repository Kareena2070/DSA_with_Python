# 287. Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.


# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:
# Input: nums = [3,3,3,3,3]
# Output: 3
 
# brute force approach
nums = [1,3,4,2,2]
def findDiplicate(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i]==nums[i+1]:
            return nums[i]

print(findDiplicate(nums))

# sort = O(n log n)
# loop = O(n)
# Total time complexity = O(n log n)
# space complexity = O(1)
# Python’s .sort() is Timsort, which requires O(1) extra space (in-place).


# better approach 
def findDiplicate1(nums):
    num_count = {}
    for num in nums:
        if num in num_count:
            num_count[num]+=1
        else:
            num_count[num]=1

    for num in num_count:
        if num_count[num] >1:
            return num
print(findDiplicate1(nums))

# Time complexity to count num = O(n)
# Time complexity of dict(num_count) = O(n)
# Total time complexity = O(n)+O(n) = O(n)

# Space complexity = O(n)  -- because dic(num_count sortes n number)


# Optimal approach 
def findDupliacte2(nums):
    num_count = {}
    for num in nums:
        if num in num_count:
            return num
        else:
            num_count[num]=1

print(findDupliacte2(nums))

# Time complexity = O(n)   -- one by pass
# Space complexity = O(n)   -- because dic(num_count sortes n number)

