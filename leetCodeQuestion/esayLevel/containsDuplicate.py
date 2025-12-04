# 217. Contains Duplicate
# level: Easy
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true



# Time Limit Exceeded
nums = [1,2,3,1]
def containsDuplicate( nums):
    for i in range(len(nums)):
        count = 0
        for j in range(len( nums)):
            if nums[i]== nums[j]:
                count+=1
        if count >1:
            return True
    return False
print(containsDuplicate(nums))
# Time Complexity = O(n^2)
# Space Complexity = O(1)

# Time Limit Exceeded
nums = [1,2,3,4]
def containsDuplicate1( nums):
    arr = []
    for i in nums:
        if i in arr:
            return True
        arr.append(i)
    return False
print(containsDuplicate1(nums))
# time Complexity = O(n^2)
# Space Complexity = O(n)
# Using a list → O(n²) total → slow → TLE (Time Limit Exceeded)

# Optimal Solution
nums = [1,2,3,1]    
def containsDuplicate2( nums):
    arr = set()
    for i in nums:
        if i in arr:
            return True
        arr.add(i)
    return False

print(containsDuplicate2(nums))
# Time Complexity = O(n)
# Space Complexity = O(n)
# Using a set → O(n) total → fast → passes