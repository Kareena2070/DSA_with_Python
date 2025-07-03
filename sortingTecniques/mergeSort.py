# Merge Sorting
# Given an array of integers, nums,sort the array in non-decreasing order using the merge sort algorithm. Return the sorted array.
# A sorted array in non-decreasing order is one in which each element is either greater than or equal to all the elements to its left in the array.
# Examples:
# Input: nums = [7, 4, 1, 5, 3]
# Output: [1, 3, 4, 5, 7]
# Explanation: 1 <= 3 <= 4 <= 5 <= 7.
# Thus the array is sorted in non-decreasing order.

# Input: nums = [5, 4, 4, 1, 1]
# Output: [1, 1, 4, 4, 5]
# Explanation: 1 <= 1 <= 4 <= 4 <= 5.
# Thus the array is sorted in non-decreasing order.

def mergeSort(nums):
    n = len(nums)-1
    merge_sort(nums, 0, n)
    return nums

def merge_sort( nums, low, high):
    if low>=high:
        return
    mid = (low+high)//2
    merge_sort(nums, low, mid)
    merge_sort(nums, mid+1, high)
    merge(nums, low, mid, high)

def merge(nums, low, mid, high):
    temp = []
    left = low
    right = mid+1
    while left<=mid and right<=high :
        if nums[left]<=nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1

    while left<=mid:
        temp.append(nums[left])
        left+=1
    while right<=high:
        temp.append(nums[right])
        right+=1

    for i in range(low, high+1):
        nums[i] = temp[i - low]



nums = [5, 4, 4, 1, 1]
nums = [7, 4, 1, 5, 3]
nums = list(map(int, input("Enter array you want to sort: ").split(",")))       #take input from user
mergeSort(nums)
print(nums)

# Time complexity 
# in merge_sort divide the array/list so it takes ("O(log n)")
# in merge, merge two  sorted array. it depen on input size so, it takes ("O(n)")
# total time complexity is = O(n log n)