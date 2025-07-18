# Move Zeros to End
# Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same. This must be done in 
# place, without making a copy of the array.
# Examples:
# Input: nums = [0, 1, 4, 0, 5, 2]
# Output: [1, 4, 5, 2, 0, 0]
# Explanation: Both the zeroes are moved to the end and the order of the other elements stay the same

# Input: nums = [0, 0, 0, 1, 3, -2]
# Output: [1, 3, -2, 0, 0, 0]
# Explanation: All 3 zeroes are moved to the end and the order of the other elements stay the same



# brute force approach
nums = [0, 0, 0, 1, 3, -2]
nums = [0, 1, 4, 0, 5, 2]
nums = [1, 2, 3,4, 5, 6,7]

def moveZero(nums):
    n = len(nums)
    temp = []
    temp2 = []
    for i in range(n):
        if nums[i] != 0:
            temp.append(nums[i])
        if nums[i] == 0:
            temp2.append(nums[i])
    return temp+temp2

print(moveZero(nums))

# Time complexity 
# loop runs on O(n) time 
# temp +temp2 take O(n) space complexity
# time complexity = O(n)
# space complexity = O(n)





# Optimal force approach

nums = [2,3,0, 1, 4, 0, 5, 2]
nums = [0, 0, 0, 1, 3, -2]

def moveZeroNum(nums):
    n = len(nums)
    j=-1
    for i in range(n):
        if nums[i]==0:
            j=i
            break
    if j == -1:
        return nums  # No zero found

    for k in range(j+1,n):
        if nums[k] !=0:
            nums[j], nums[k] = nums[k], nums[j]
            j+=1

    return nums

print(moveZeroNum(nums))


# Time Complexity
# loop 1 runs for O(n)
# loop 2 runs for 0(n)
# total time complexity = O(n)+O(n) == O(n)
# space complexity is 0(1)
