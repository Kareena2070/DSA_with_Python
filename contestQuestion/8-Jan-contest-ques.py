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


# ques 3.

# Movie Hype
# Chef decided to watch a movie, and has just entered the theater.

# The theater has 2N+12N+1 seats arranged in a row. The seats are numbered 1 to 2N+12N+1 from left to right.

# Currently, the seats numbered 
# 1,3,5,7,…,2N+1,3,5,7,…,2N+1 are occupied, and the seats numbered 2,4,6,…,2N2,4,6,…,2N are empty.
# Chef must decide which empty seat to sit in.

# For each i=1,2,3,…,N+1 i=1,2,3,…,N+1, The person sitting in seat 2i−1 2i−1 has a hype level of A i.That is, the person in seat 1 has a hype level of A 1, the person in seat 3 has a hype level of A 2 , and so on.

# Chef thinks the loudness of an empty seat is the maximum of the hype levels of the two people sitting next to him.
# So, the loudness of seat 2 is the maximum of the hype levels of the people sitting in seats 1 and 3; the loudness of seat 4 is the maximum of the hype levels of the people sitting in seats 3 and 5; and so on.

# To properly enjoy the movie, Chef would like to choose a seat whose loudness is as low as possible.

# Can you help Chef by finding this minimum loudness?


t = int(input('Number of test cases: '))

for _ in range(t):
    n = int(input('Number of people: '))
    a = list(map(int, input('seats: ').split()))
    
    min_loud = float('inf')
    
    for i in range(n):
        current_loud = max(a[i], a[i+1])
        if current_loud < min_loud:
            min_loud = current_loud
    print(min_loud)