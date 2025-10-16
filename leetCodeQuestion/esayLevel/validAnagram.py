# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

s = "anagram"
t = "nagaram"

from collections import Counter
def isAnagram(s, t):
    freq1 = Counter(s)
    freq2 = Counter(t)
    if freq1 == freq2:
        return True
    else:
        return False
    
print(isAnagram(s, t))
# Time complexity = O(n+m) n = length of s and m = length of t
# space complexity = O(n+m) for storing frequency of both strings
