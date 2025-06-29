# Check if String is Palindrome or Not
# Given a string s, return true if the string is palindrome, otherwise false.
# A string is called palindrome if it reads the same forward and backward.

# Examples:
# Input : s = "hannah"
# Output : true
# Explanation : The string when reversed is --> "hannah", which is same as original string , so we return true.

# Input : s = "aabbaaa"
# Output : false
# Explanation : The string when reversed is --> "aaabbaa", which is not same as original string, So we return false.


name = input("Enter your name: ")

def palindrome(name):
    n = len(name)
    def sIndex(i):
        if i > n//2:
            return True
        if name[i] != name[n-i-1]:
            return False
        return sIndex(i+1)
    return sIndex(0)
    
print(palindrome(name))




# if in any input there is non-alphanumeric (like ","; ":") ignore this for that use below code 
# s = ''.join(ch.lower() for ch in s if ch.isalnum())

def isPalindrome(s):
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    n = len(s)
    def sIndex(i):
        if i >=n//2:
            return True 
        if s[i] != s[n-i-1]:
            return False
        return sIndex(i+1)
    return sIndex(0)
print(isPalindrome("A man, a plan, a canal: Panama"))