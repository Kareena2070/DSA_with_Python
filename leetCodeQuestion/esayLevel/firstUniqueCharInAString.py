# 387. First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

s = "loveleetcode"

# Brute Force Solution
def firstUniqCharBruteForce(s):
    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                count+=1
        if count ==1:
            return i
    return -1
print(firstUniqCharBruteForce(s))
# Time Complexity: O(n^2)
# Space Complexity: O(1)




# Optimized Solution
from collections import Counter
def firstUniqChar(s):
    count = Counter(s)

    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
    return -1

print(firstUniqChar(s))
# Time Complexity: O(n)   (dictionary - O(n)- woerse case + loop O(n))
# Space Complexity: O(1)
