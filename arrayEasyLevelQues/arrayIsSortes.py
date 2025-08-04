# Given an array, check if it is sorted in non-decreasing order.
# Example:
# [1, 2, 2, 3] → True
# [1, 3, 2, 4] → False

arr = [1, 2, 3, 4, 5]
arr = [1, 3, 2, 4]

def is_sorted(arr):
    n = len(arr)
    for j in range(1, n ):
        if arr[j] < arr[j-1]:
            return False
    return True

print(is_sorted(arr))






