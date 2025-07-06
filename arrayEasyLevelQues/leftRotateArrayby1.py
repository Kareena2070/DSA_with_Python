# Left Rotate Array by One
# Given an integer array nums, rotate the array to the left by one.
# Note: There is no need to return anything, just modify the given array.
# Examples:
# Input: nums = [1, 2, 3, 4, 5]
# Output: [2, 3, 4, 5, 1]
# Explanation: Initially, nums = [1, 2, 3, 4, 5]
# Rotating once to left -> nums = [2, 3, 4, 5, 1]

# Input: nums = [-1, 0, 3, 6]
# Output: [0, 3, 6, -1]\
# Explanation: Initially, nums = [-1, 0, 3, 6]
# Rotating once to left -> nums = [0, 3, 6, -1]



nums = [1, 2, 3, 4, 5]

def leftRotate(nums):
    n = len(nums)
    temp = nums[0]
    for i in range(1, n):
        nums[i-1]= nums[i]
    nums[n-1]= temp
    return nums

leftRotate(nums)
print(nums)

# Time complexity 
# here only one loop is running till n so Time complexity is O(n)
# improtant:
# in algorithm space complexity is 0(n) beacuse we use whole array to solve the question 
# but in appraoch space complexity is O(1) because we don't use any extra space, we use same array to solve the question