# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# brute froce approach

nums = [1,2,3,4]

def productExceptSelf(nums):
    arr = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i == j:
                continue
            else:
                product = product*  nums[j]
        arr.append(product)
    return arr 

print(productExceptSelf(nums))

# Time complexity = O(n^2)
# space complexity = O(n)


def productExceptSelf1(nums):
    n = len(nums)
    prefix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i-1]*nums[i-1]

    suffix = [1]*n
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    result = [0]*n
    for i in range(n):
        result[i] = prefix[i]*suffix[i]
    
    return result

print(productExceptSelf1(nums))

# Time complexity = O(n)+O(n)+O(n) == O(n)
# space complexity = O(n)