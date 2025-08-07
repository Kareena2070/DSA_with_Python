#Check if String is Palindrome

word = "madam"

def palindrome1(string):
    oldStr = string
    newStr = []
    for i in range(len(string)-1, -1, -1):
        newStr.append(string[i])

    palindromeStr = "".join(newStr)

    if oldStr == palindromeStr:
        print(True)
    else:
        print(False)
palindrome1(word)

# time complexity 
# loop runs O(n)
# append takes O(1)
# join takes O(n)
# tring comparison (oldStr == palindromeStr):
# Compares two strings of length n.→ Total: O(n)
# so total time complexity = O(n)

# newStr list stores all n characters → O(n)
# palindromeStr is a new string of length n → O(n)
# Other variables (oldStr) just point to the same memory, so no extra space.
# space complexity = O(n)



def palindrome2(string):
    if string == string[::-1]:
        print(True)
    else:
        print(False)

palindrome2(word)

# time complexity 
# string[::-1] Python creates a new reversed string, character by character.→ Time: O(n)
# Compares two strings of length n.→ Time: O(n)
# so, total time complexity = O(n)

# pace Complexity
# string[::-1] creates a new reversed string → takes O(n) space.
# Original string is reused → no extra space.
# so, space complesxity = O(n)