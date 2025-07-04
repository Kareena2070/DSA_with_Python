# Quick Sorting
# Given an array of integers called nums, sort the array in non-decreasing order using the quick sort algorithm and return the sorted array.
# A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
# Examples:
# Input: nums = [7, 4, 1, 5, 3]
# Output: [1, 3, 4, 5, 7]
# Explanation: 1 <= 3 <= 4 <= 5 <= 7.
# Thus the array is sorted in non-decreasing order.

# Input: nums = [5, 4, 4, 1, 1]
# Output: [1, 1, 4, 4, 5]
# Explanation: 1 <= 1 <= 4 <= 4 <= 5.
# Thus the array is sorted in non-decreasing order.


nums = [5, 4, 4, 1, 1]
nums = list(map(int, input("Enter a array and use ',': ").split(",")))

def quickSort(nums):
    def partition(nums, low, high):
        pivot = nums[low]
        i = low
        j = high
        while i <j:
            while i <=high-1 and nums[i]<=pivot:
                i+=1
            while j >= low+1 and nums[j]>pivot:
                j-=1
            if i <j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[low], nums[j] = nums[j], nums[low]
        return j 

    def qs( nums, low, high):
        if low <high:
            pIndix = partition(nums, low, high)
            qs(nums, low, pIndix-1)
            qs(nums, pIndix+1, high)
        return nums

    return qs(nums, 0, len(nums)-1)

quickSort(nums)
print(nums)


# Time Complexity
# in first function while loop is runing n time so, O(n)
# in second function diving the array in 2 parts so, O(log n)
# total time complexity is O(n)+O(log n) = O(n log n)
