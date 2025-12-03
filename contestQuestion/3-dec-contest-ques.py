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
