# Find missing number
# Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.
# Examples:
# Input: nums = [0, 2, 3, 1, 4]
# Output: 5
# Explanation: nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

# Input: nums = [0, 1, 2, 4, 5, 6]
# Output: 3
# Explanation: nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]

nums = [0, 2, 3, 1, 4]
# nums = [0, 1, 2, 4, 5, 6]


# Brute Force - Double Loop
def missingNum(nums):
    n = len(nums)
    for i in range(1, n+1):
        flag = 0
        for j in range(0,n):
            if nums[j] == i:
                flag = 1
                break
        if flag ==0:
            return i

print(missingNum(nums))

# Time complexity
# here two loops are runing so Time domplexity is O(n1*n2) = O(N^2)
# space complexity is O(1) no extra space





