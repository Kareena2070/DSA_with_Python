# Find First Non-Repeating Character

word = "kareena"

def nonRepeating(word):
    for i in range(len(word)):
        count = 0
        char = word[i]
        for j in range(len(word)):
            if char == word[j]:
                count+=1
        if count == 1:
            print(char)
            break

nonRepeating(word)

# time complexity 
# outer loop runs O(N) time and also inner loop runs O(N) times 
# so total time complexity = O(n^2)
# space complexity is = O(n), no such extra space added

     
        