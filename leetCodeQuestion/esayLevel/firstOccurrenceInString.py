
# 28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.



h = "sadbutsad"
n = "sad"

h = "leetcode"
n = "leeto"

def OccurenceString(h, n):
    if n == "":
        return 0
    for i in range(len(h)-len(n)+1):
        match = True
        for j in range(len(n)):
            if h[i+j] !=n[j]:
                match = False
                break
        if match:
            return i
    return -1



print(OccurenceString(h, n))

# Time complexity = O(m*n)
# space complexity = O(1)
