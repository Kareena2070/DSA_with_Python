# Reverse an array
# Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.
# Examples:
# Input: n=5, arr = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Explanation: The reverse of the array [1,2,3,4,5] is [5,4,3,2,1]

# Input: n=6, arr = [1,2,1,1,5,1]
# Output: [1,5,1,1,2,1]
# Explanation: The reverse of the array [1,2,1,1,5,1] is [1,5,1,1,2,1].

arr = list(input("Enter a areay: ").split(","))

def reverseAarray(i, arr):
    n = len(arr)
    if i >= n//2:
        return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    reverseAarray(i+1, arr)

print(reverseAarray(0, arr))
print(arr)



# this is done according to the question 

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array elements separated by commas: ").split(",")))

def reverse(arr, n):
    def helpNum(i):
        if i>=n//2:
            return
        arr[i], arr[n-i-1]= arr[n-i-1], arr[i]
        helpNum(i+1)
    helpNum(0)

reverse(arr, n)
print(arr)

