# 485. Max Consecutive Ones
# level: Easy
# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]

def findMaxConsecutiveOnes( nums):
        count = 0
        arr = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                arr.append(count)
                count = 0
            if i == len(nums)-1:
                arr.append(count)
        num = max(arr)
        return num
print(findMaxConsecutiveOnes(nums))

# Time Complexity = O(n)
# Space Complexity = O(n) -- arr stores count of 1's sequences
