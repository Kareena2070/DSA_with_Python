#ques 1.
# New Year Resolution
# To start the year 2026 off, Chef made a resolution to exercise daily. He decided to do exactly X push-ups every day.

# If he sticks to his resolution, how many push-ups will he do in the month of January?
# Note that the month of January has 31 days.

x = int(input('Number of push-ups per day: '))

print(x*31)



# ques 2.
# Front-Back Matching
# You are given a string S of length N.The string contains only lowercase English letters.

# You can freely rearrange the characters of S however you like.

# After rearrangement, is it possible to make the first and last characters of S equal?

t = int(input('Number of test cases: '))

for _ in range(t):
    n = int(input('Length of string: '))
    s = input('String: ')
    r = len(set(s))
    if r < len(s):
        print('Yes')
    else:
        print('No')
