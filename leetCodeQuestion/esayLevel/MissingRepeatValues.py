# 2965. Find Missing and Repeated Values
# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

# Example 1:

# Input: grid = [[1,3],[2,2]]
# Output: [2,4]
# Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

# Example 2:
# Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
# Output: [9,5]
# Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].



grid = [[9,1,7],[8,9,2],[3,4,6]]
# grid = [[1,3],[2,2]]
from collections import Counter
def findMissingRepeatedValues(grid):
    arr = []
    ans = []
    for sub in grid:
        for i in sub:
            arr.append(i)
    
    freq = Counter(arr)
    for num, count in freq.items():
        if count == 2:
            ans.append(num)
            break

    n = len(grid)
    full = set(range(1, n*n + 1))
    missing = list(full - set(arr))[0]
    ans.append(missing)
    
    return ans

print(findMissingRepeatedValues(grid))


# Time complexity = O(n^2)
# for merge arr = O(n^2)
# for find repeated num = O(n^2)
# for missing num = O(n^2)
# so total time complexity is O(n^2)+O(n^2)+O(n^2) = O(n^2)   --- 3 pass(O(n^2))