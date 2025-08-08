#  Count Vowels in a String

name = "kareena"
def vowels1(string):
    count = 0
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
            count+=1
    print(count)
vowels1(name)


# time complexity
# one loop runs = O(n)
# space complexity
# not storing any extra data = O(1)




