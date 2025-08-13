#  Remove Duplicates from String

word = "bcabc123!@#"

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

