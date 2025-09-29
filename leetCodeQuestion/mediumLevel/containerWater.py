# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Brute force Approach
height = [1,8,6,2,5,4,8,3,7]

def maxArea(height):
    n = len(height)
    max_area = 0
    for i in range(n):
        for j in range(i+1, n):
            area = (j-i) * min(height[i], height[j])
            max_area = max(max_area, area)
    return max_area

print(maxArea(height))

# Time conplexity = O(n^2)
# Space complexity = O(1)



def maxArea1(height):
    left = 0
    right = len(height)-1
    max_area =0
    while left <right:
        area = (right-left) * min(height[left], height[right])
        max_area = max(max_area, area)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max_area

print(maxArea1(height))

# Time complexity = O(n)  - use Two pointer
# space comoplexity = O(1)