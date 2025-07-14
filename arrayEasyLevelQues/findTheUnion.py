# Union of two sorted arrays
# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.
# The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.
# Examples:
# Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
# Output: [1, 2, 3, 4, 5, 7]
# Explanation: The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

# Input: nums1 = [3, 4, 6, 7, 9, 9], nums2 = [1, 5, 7, 8, 8]
# Output: [1, 3, 4, 5, 6, 7, 8, 9]
# Explanation: The element 7 is common to both, 3, 4, 6, 9 are from nums1 and 1, 5, 8 is from nums2


# brute Force
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [1, 2, 7]
# nums1 = [3, 4, 6, 7, 9, 9]
# nums2 =[1, 5, 7, 8, 8]

# def unionNum(nums1, nums2):
#     result = []
#     seen = {}
#     for num in nums1 + nums2:
#         if num not in seen:
#             result.append(num)
#             seen[num] = True
#     return result

# print(unionNum(nums1, nums2))




# Optimal approach 

def find_union(arr1, arr2):
    i, j = 0, 0  # Pointers
    union = []  # Union list

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  # Case 1 and 2
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:  # Case 3
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < len(arr1):  # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):  # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


arr1 = [1, 2, 3, 4, 5, 6,6, 6, 6, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

# union = find_union(arr1, arr2)
print(find_union(arr1, arr2))
