# In an array find the second largest and second smallest number 

# nums = list(map(int, input("Enter an array: ").split()))

nums = [4, 345, 345,34567, 34,234,345,23, 12, 345, 2, 8, 2, 234]

nums = [8, 8, 7, 6, 5]
def secondLargest(nums):
    n = len(nums)
    largestNum = nums[0]
    secondLargestNum = -1

    for i in range(n):
        if nums[i] > largestNum:
            secondLargestNum = largestNum
            largestNum = nums[i]
        elif nums[i]<largestNum and nums[i] > secondLargestNum:
            secondLargestNum = nums[i]
    return secondLargestNum

print(secondLargest(nums))


def secondSmallest(nums):
    n  = len(nums)
    smallestNum = nums[0]
    secondSmallestNum = -1

    for i in range(n):
        if nums[i]< smallestNum:
            secondSmallestNum = smallestNum
            smallestNum = nums[i]
        elif nums[i]> smallestNum and nums[i] < secondSmallestNum:
            secondSmallestNum = nums[i]
    return secondSmallestNum

print(secondSmallest(nums))

            