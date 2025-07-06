# Check if the Array is Sorted II
# Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.
# Examples:
# Input : nums = [1, 2, 3, 4, 5]
# Output : true
# Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

# Input : nums = [1, 2, 1, 4, 5]
# Output : false
# Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.


nums = list(map(int,input("Enter 5 number: ").split(",")))         # take input from the user 
n = len(nums)
for i in range(1, n):
    if nums[i]<=nums[i-1]:
        print( False)
        break
else:
    print(True)



# T = int(input("Enter the array size: "))
# for _ in range(T):
#     nums = list(map(int,input("Enter 5 number: ").split()))
 