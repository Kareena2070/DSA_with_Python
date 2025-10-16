# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    common = ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        
        for string in strs:
            if i >= len(string) or string[i] != char:
                return common
        common += char
    return common
print(longestCommonPrefix(strs))

# Time complexity = O(n*m) length of string * length of first word
# Space complexity = O(m) where m is the length of the common prefix
