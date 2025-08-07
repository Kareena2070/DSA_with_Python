#  Reverse a String

name = "navgurukul is my best place"
def reverseString1(string):
    revserString = string[::-1]
    print(revserString)

reverseString1(name)

# ✅ Time Complexity
# Python slicing string[::-1] internally creates a new string, copying characters in reverse order.
# It must go through all n characters once →
# 🕒 Time = O(n)
# ✅ Space Complexity
# Creates a new reversed string → occupies n space.
# Original string is not modified.
# 🧠 Space = O(n)


def reverseString2(string):
    n = len(string)
    newString = ""
    for i in range(n-1, -1, -1):
        newString+=string[i]
    print(newString)
reverseString2(name)

# ✅ Time Complexity
# Loop runs n times → that part is O(n)
# But newString += string[i] creates a new copy every time (since strings are immutable in Python) → O(n) for each += step
# So the full loop becomes:O(1 + 2 + 3 + ... + n) = O(n²)
# 🕒 Time = O(n²) ← slower
# ✅ Space Complexity
# One final string of length n is returned.
# Intermediate temporary strings are garbage collected.
# 🧠 Space = O(n)


def reverseString3(s):
    chars = []
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])
    return ''.join(chars)
print(reverseString3(name))

# time complexity 
# append() + ''.join() → O(n) time
# append() adds one character to a list in O(1).
# join() combines the list into one string in a single pass (O(n)).
# space complexity = O(n)
# append + join only uses one list and one final string — more memory-efficient in practice.