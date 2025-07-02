# Counting Frequencies of Array Elements
# Given an array nums of size n which may contain duplicate elements, return a list of pairs where each pair contains a unique element from the array and its frequency in the array.
# You may return the result in any order, but each element must appear exactly once in the output.

# Examples:
# Input: nums = [1, 2, 2, 1, 3]
# Output: [[1, 2], [2, 2], [3, 1]]
# Explanation:
# - 1 appears 2 times
# - 2 appears 2 times
# - 3 appears 1 time
# Order of output can vary.

# Input: nums = [5, 5, 5, 5]
# Output: [[5, 4]]
# Explanation:
# - 5 appears 4 times.

from collections import defaultdict
arr = [1, 2, 2, 1,3]
arr = [5,5,5,5]
result = []

freq = defaultdict(int)
for num in arr:
    freq[num]+=1

for key, value in freq.items():
    result.append([key, value])

print(result)



