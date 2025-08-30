# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
 
nums = [0,1,0,3,12]  
one = []
zero =[]
for i in range(len(nums)):
    if nums[i]>0:
        one.append(nums[i])
    else: 
        zero.append(nums[i])
    
print(one+zero)

# time complexity = O(n)
# space complexity = O(n)+ O(n) = O(n)

def num(nums):
    num = 0
    for i in range(len(nums)):
            for j in range( -1,len(nums)):
                if nums[j] ==0:
                    nums[j], nums[i] = nums[i], nums[j]
    return nums

nums = [0,1,0,3,12]    
print(num(nums))

# time complexity = O(n^2)
# space complexity = O(1)

