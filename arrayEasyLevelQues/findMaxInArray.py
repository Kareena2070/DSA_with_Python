# Find Max in Array

arr = [2, 5, 8, 2, 4, 678, 89,345, 23, 56, 78, 90, 100, 200, 300]
arr = [5, 19, 30, 56, 23, 1, 6]

def findMax(arr):
    n = len(arr)
    maxNum = arr[0]
    for i in range(1, n):
        if maxNum < arr[i]:
            maxNum = arr[i]
    return maxNum
print(findMax(arr))

# Time complexity is = O(n)  => one loop is used
# Space Complexity = O(1) => no extra space is used



