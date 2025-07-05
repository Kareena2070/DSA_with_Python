# Second Largest Element
# Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

# Examples:
# Input: nums = [8, 8, 7, 6, 5]
# Output: 7
# Explanation: The largest value in nums is 8, the second largest is 7

# Input: nums = [10, 10, 10, 10, 10]
# Output: -1
# Explanation: The only value in nums is 10, so there is no second largest value, thus -1 is returned

# Brute force 
nums = [8, 8, 7, 6, 5]
nums = [10, 10, 10, 10, 10]
n = len(nums)
for i in range(n, 1, -1):
    for j in range(i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
sortNum = nums
largest = sortNum[n-1]
for el in range(n-2, 0, -1):
    if sortNum[el]!=largest:
        print(sortNum[el])
        break
else:
    print(-1)
        
# Time Complexity 
# in 1st loop, outer loop runs n-1 time, inner loop n-1 time so, this loop runs O(n^2)
# in 2nd loop run n-1 time so, O(n)
# total time complexity is O(n^2)+O(n) == O(n^2)


