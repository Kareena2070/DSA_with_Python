#  Check if Array Is Sorted and Rotated
# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].
# Example 2:

# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.
# Example 3:

# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.


# nums = list(map(int,input("enter your array: ").split(" ")))

nums = [3,4,5,1,2]

def CheckSorted(nums):
    n = len(nums)
    count = 0

    for i in range(n):
        if nums[i]>nums[(i+1)%n]:
            count+=1
            if count>1:
                return False
    return True

print(CheckSorted(nums))


# Time complexity 
# one loop is running so, O(n)
# one variable count but no extra space proportional to input size so, O(1)

