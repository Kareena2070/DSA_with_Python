# Remove duplicates from sorted array
# Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once. Return the number of unique elements in the array.
# If the number of unique elements be k, then,
# Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
# The remaining elements, as well as the size of the array does not matter in terms of correctness.
# An array sorted in non-decreasing order is an array where every element to the right of an element is either equal to or greater in value than that element.
# Examples:
# Input: nums = [0, 0, 3, 3, 5, 6]
# Output: 4
# Explanation: Resulting array = [0, 3, 5, 6, _, _]
# There are 4 distinct elements in nums and the elements marked as _ can have any value.

# Input: nums = [-2, 2, 4, 4, 4, 4, 5, 5]
# Output: 4
# Explanation: Resulting array = [-2, 2, 4, 5, _, _, _, _]
# There are 4 distinct elements in nums and the elements marked as _ can have any value.


# nums = list(map(int, input("Enter your array: ").split()))
# nums = [-2, 2, 4, 4, 4, 4, 5, 5]
nums = [0, 0, 3, 3, 5, 6, 7, 8]

# brute force
def removeDuplicate(nums):
    n = len(nums)
    st = set()
    for i in range(n):
        st.add(nums[i])
    k = len(st)
    return k 

print("The array after removing duplicate elements is ", removeDuplicate(nums))


# Time complexity 
# in set if we insert/add element it takes O(n log n)
# a loop also runs it take O(n)
# as in time complexity we ignore smaller time so total time complexity is O(n log n)+O(n) == O(n log nn)
# space complexity is 0(n)  because every number will check


