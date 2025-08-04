# Reverse an array

arr = [ 1, 2, 3, 4, 5, 6, 7]
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
arr = [12, 45, 2, 4]

def reverseArray(arr):
    n = len(arr)
    new_arr = []
    for i in range(n-1, -1, -1):
        new_arr.append(arr[i])

    return new_arr
     
print(reverseArray(arr))
# Time complexity = O(n)  => one loop is used
# Space complexity = O(n) => whole array will again store in new variable




