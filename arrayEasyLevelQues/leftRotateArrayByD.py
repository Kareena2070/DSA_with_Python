# Left Rotate Array by K Places

# Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.
# Examples:
# Input: nums = [1, 2, 3, 4, 5, 6], k = 2
# Output: nums = [3, 4, 5, 6, 1, 2]
# Explanation: rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
# rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]

# Input: nums = [3, 4, 1, 5, 3, -5], k = 8
# Output: nums = [1, 5, 3, -5, 3, 4]
# Explanation: rotate 1 step to the left: [4, 1, 5, 3, -5, 3]
# rotate 2 steps to the left: [1, 5, 3, -5, 3, 4]
# rotate 3 steps to the left: [5, 3, -5, 3, 4, 1]
# rotate 4 steps to the left: [3, -5, 3, 4, 1, 5]
# rotate 5 steps to the left: [-5, 3, 4, 1, 5, 3]
# rotate 6 steps to the left: [3, 4, 1, 5, 3, -5]
# rotate 7 steps to the left: [4, 1, 5, 3, -5, 3]
# rotate 8 steps to the left: [1, 5, 3, -5, 3, 4]



# brute Force
nums = [1, 2, 3, 4, 5, 6]
k = 15
n = len(nums)
k = k%n                         #here we use this because if k is more then the length of array so it can give really number to rotate
temp = nums[0:k]
for i in range(k, n):
    nums[i-k] = nums[i]
for j in range(n-k,n):
    nums[j] = temp[j-(n-k)]
print(nums)


# Final Time Complexity
# Modulo operation	                            O(1)
# Creating temp array	                        O(k)
# Shifting left by k elements	                O(n - k)
# Appending temp at end                     	O(k)

# Total Time Complexity: O(n)
# Because k + (n - k) + k = n + k, and in Big-O notation, we drop constants, so it's O(n).
# Space Complexity = O(k)



# Optimal force solution




