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




# solve without any space 

def reverse_array(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    return arr
print(reverse_array(arr))
# Time complexity = O(n)
# space complexity = O(1)


# Pythonic way:
def reverseArray(arr):
    return arr[::-1]

print(reverseArray(arr))
# time complexity = O(n)
# Space Complexity= O(n)