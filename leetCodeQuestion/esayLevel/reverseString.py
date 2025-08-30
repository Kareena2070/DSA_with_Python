# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


# brute fore approach
s = ["h","e","l","l","o"]
def reverseString(s):
    n = len(s)
    string = []
    for i in range(n-1, -1, -1):
        string.append(s[i])
    return string

print(reverseString(s))
# time complexity = O(n)
# Space complexity - O(n)




