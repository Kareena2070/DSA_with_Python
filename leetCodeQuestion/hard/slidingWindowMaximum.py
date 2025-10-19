# 239. Sliding Window Maximum

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# brute force approach
nums = [1,3,-1,-3,5,3,6,7]
k = 3
def maxSlidingWindow(nums, k):
    n = len(nums)
    if n == 0:
        return []
    elif n == 1:
        return nums
    elif k>=n:
        return [max(nums)]
    
    arr = []
    for i in range(n-k+1):
        num = max(nums[i:i+k])
        arr.append(num)
    return arr

print(maxSlidingWindow(nums, k))
# Time complexity = O(n*k) where n is the length of the nums array and k is the size of the sliding window.
# Space complexity = O(n-k+1) for storing the result array.
