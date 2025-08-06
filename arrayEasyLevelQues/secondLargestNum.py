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
nums = [1, 2, 3, 4, 5]
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
    print("Not found second largest number so it will: ",-1)
        
# Time Complexity 
# in 1st loop, outer loop runs n-1 time, inner loop n-1 time so, this loop runs O(n^2)
# in 2nd loop run n-1 time so, O(n)
# total time complexity is O(n^2)+O(n) == O(n^2)





# Better force
nums = [8, 8, 7, 6, 5]
# # nums = [10, 10, 10, 10, 10]
# nums = [1, 2, 3, 4, 5]
largest = nums[0]
n = len(nums)
for i in range(n):
    if nums[i]>largest:
        largest = nums[i]

secondLargest = -1
for j in range(n):
    if nums[j] >secondLargest and nums[j]!= largest:
        secondLargest = nums[j]
        print("Second Largest Number is: ", secondLargest)
        break
else:
    if secondLargest == -1:
        print("Not found second largest number so it will: ",-1)

# Time complexity 
# 1st loop runs for O(n) time 
# 2nd loop runs for O(n) time 
# total time complexity is 0(n+n) =O(2n) that is O(n) only
# improtent ( O(n) + O(n) = O(n) → Two passes through the array.)









# Optimal force
nums = [8, 8, 7, 6, 5]
# nums = [10, 10, 10, 10, 10]
# nums = [1, 2, 3, 4, 5]
n = len(nums)
largestNum = nums[0]
secondLargestNum = -1
for i in range(n):
    if nums[i] > largestNum:
        secondLargestNum = largestNum
        largestNum = nums[i]

    elif nums[i]<largestNum and nums[i] >secondLargestNum:
        secondLargestNum = nums[i]
        print("Second Largest element in array: ", secondLargestNum)

else:
    if secondLargestNum ==-1:
        print("Second largest number NOT found in array so: ",-1)

# Time Complexity 
# on loop runs so it time complexity is O(n)
# important ( O(n) → One pass through the array.)


# most Optimal approch that can solve a sorted array's second largest num
# nums = [8, 8, 7, 6, 5]
# nums = [12, 35, 10, 34, 1]
# nums = [1, 2, 3, 4, 5]
# nums = [10, 10, 10, 10, 10]
nums = [2, 4, 2, -4, -1, 6]

def secondLargest(nums):
    if len(nums) <2:
        return "Array too short", None

    largest = nums[0]
    secondNum = float('-inf')
    
    for i in range(1, len(nums)):
        if nums[i]> largest:
            secondNum = largest
            largest = nums[i]
        elif nums[i] > secondNum and nums[i] != largest:
            secondNum = nums[i]

    if(secondNum == float('-inf')):
        return "not found", -1
    else:
        return 'Second largest number in an array:',secondNum
    
print(secondLargest(nums))

# time complexity = O(N) 
# Space complexity = O(1)

