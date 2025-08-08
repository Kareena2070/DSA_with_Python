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


def vowels2(string):
    count = 0
    for i in range(len(string)):
        if string[i] in "aeiouAEIOU":
            count+=1
    print(count)
vowels2(name)

# time one loop runs = O(n)
# space complexity = O(1)

def count_vowels(string):
    vowels = set("aeiouAEIOU")
    count = 0
    for ch in string:
        if ch in vowels:
            count += 1
    print(count)

name = "kareena"
count_vowels(name)


