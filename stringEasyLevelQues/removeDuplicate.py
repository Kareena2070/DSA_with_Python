#  Remove Duplicates from String

word = "bcabc123!@#"


# brute force approach

def removeDuplicate(word):
    duplicate = ""
    for i in word:
        if i not in duplicate:
            duplicate+=i
    print(duplicate)

removeDuplicate(word)
# Timecomplexity 
# outer loop runs O(n)
# inter loop runs O(n) => check each char in duplicate
# total time complexity === O(n)
# Space complexity === O(n) 



# better approch
def remove(word):
    string = set(word)
    print("".join(string))

remove(word)
# time complexity === O(n)
# space complexity === O(n) because join (joining the set back into a string )
# ⚠ But order of characters is not guaranteed.


# optimal approcah 
def remove(word):
    seen = set()
    result = []
    for ch in word:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    print("".join(result))

word = "banana"
remove(word)
# set ==  O(1) space allocation
# outer loop == O(n) iterations
#  if condition == O(1) average
# add === O(1) average
# space complexity ===O(n)



# Pythonic One-Liner
word = "banana"
print("".join(dict.fromkeys(word)))  # Output: ban

# Final Time Complexity: O(n)
#  Space Complexity: O(n) (dictionary + output string)

