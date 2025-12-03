# 1. Competition of 4
# You are participating in an elite chess tournament for 4 people in the world only.

# There are prizes in this tournament, obviously. If you finish rank i, you get 1000⋅24−i 1000⋅2 4−i rupees. Thus, the prizes are as follows:

# Rank 1: 8000 rupees
# Rank 2: 4000 rupees 
# Rank 3: 2000 rupees
# Rank 4: 1000 rupees
# You finished at rank X. How much prize money did you win?

x = int(input("what is your rank? "))
if x == 1:
    print(8000)
elif x == 2:
    print(4000)
elif x == 3:
    print(2000)
else:
    print(1000)

# 2. Gem Bundles
# You have R red gems, B blue gems and G green gems. Each gem normally sells for 3 coins.
# However, if you make a bundle of 1 red gem, 1 blue gem and 1 green gem; you can sell it for 10 coins instead.
# What is the maximum number of coins you can earn?

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# The first and only line of input contains 3 integers - R, B and G.

# Output Format
# For each test case, output on a new line the maximum number of coins you can earn.

t = int(input("number of test cases: "))
for _ in range(t):
    r, b, g = list(map(int, input("red gem, blue gem, green gem: ").split()))
    num = min(r, b, g)
    
    left = (r-num)+(b-num)+(g-num)
    bundle = num*10
    print("Total coins: ",(left*3)+bundle)
    
