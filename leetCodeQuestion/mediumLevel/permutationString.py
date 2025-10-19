# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

s1 = "ab"
s2 = "eidbaooo"

# brute force approach
def checkInclusion(s1, s2):
        n = len(s2)
        m = len(s1)
        for i in range(n-m+1):
            arr = s2[i:i+m]
            if sorted(arr) == sorted(s1):
                return True
            
        return False
print(checkInclusion(s1, s2))
# Time complexity = O(n*m log m) where n is the length of s2 and m is the length of s1.
# Space complexity = O(m) for storing the substring of s2 of length m.

