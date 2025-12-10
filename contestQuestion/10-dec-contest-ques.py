# Ques 1. Entertainments
# Chef is trying to entertain 
# N children. He has 2 options:
# Buy a single television for all the children to watch. This will cost 1000 rupees.
# Buy N toys, one for each child. This will cost 200 rupees for each toy.
# What is the minimum cost Chef needs to pay to entertain all the children?

# Input Format
# The first and only line of input contains a single integer N - the number of children.

# Output Format
# Output the cost to entertain all children.


n = int(input("number of children: "))
k = n*200
if k <1000:
    print(k)
else:
    print(1000)

#Ques 2.  Scoring
# Alice and Bob were playing a game with points to score. Each player's score is some non-negative integer number of points.

# In the end, Alice won the game by scoring X more points than Bob. Further, it is known that the total number of points scored by both of them was Y.

# With this information, your task is to find how many points Alice scored, and how many points Bob scored. It is guaranteed that the input is generated such that there exists a valid solution.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# The first and only line of each test case contains 2 integers - X and Y.
# Output Format
# For each test case, output on a new line Alice and Bob's scored points.

t = int(input("number of test cases: "))
for _ in range(t):
    x, y = list(map(int, input("Alice extra points and total points: ").split()))
    
    k = y-x
    l = k//2
    r = x+ l 
    m = y-r
    print("Alice points:", r, "Bob points:", m)
    


# Best Seats
# Chef and Chefina are trying to watch a cricket game. They have already decided a row of N seats where they will seat, but they are yet to figure out the exact 2 seats they will buy.

# The i-th seat in the row costs AiA i​coins to buy. Obviously, they have to sit next to each other, so they will only buy adjacent seats.

# Can you figure out the minimum cost for them to buy 2 seats such that they are able to sit together?

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of multiple lines of input.
# The first line of each test case contains a single integer N - the number of seats in the row.
# The second line contains    N integers - A1,A2,A3,......AN.
# Output Format
# For each test case, output on a new line the minimum cost of buying 2 adjacent seats.


t = int(input("number of test cases: "))
for _ in range(t):
    n = int(input("Number of seats: "))
    a = list(map(int, input("Seat numbers left: ").split()))
    arr = []

    for i in range(len(a)-1):
        total = a[i]+a[i+1]
        arr.append(total)
            
    num = min(arr)
    print(num)
            