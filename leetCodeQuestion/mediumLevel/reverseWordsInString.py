# 151. Reverse Words in a String

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

s = "  hello world  "
def reverseWords(s):
    words = s.split()
    words.reverse()
    return " ".join(words)
print(reverseWords(s))

# Time complexity
# split() function takes O(n) time where n is the length of the string.
# reversing the list of words takes O(m) time where m is the number of words.
# join() function takes O(n) time.
# Overall time complexity is O(n).
# Space complexity
# We are using extra space to store the list of words, which takes O(m) space where m is the number of words.
# Therefore, the space complexity is O(m).