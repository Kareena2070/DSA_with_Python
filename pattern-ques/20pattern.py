n = 5
for i in range(0, n+1):
    # left side
    for j in range(n-i+1, n+1):
        print("*", end="")
    # space
    for k in range((n-i)*2):
        print(" ", end="")
#     # right side
    for j in range(1,i+1):
        print("*", end="")
    print()

for i in range(1, n):
    # left side
    for j in range(1,n-i+1):
        print("*", end="")
    # space
    for k in range(i*2):
        print(" ", end="")
    # left side
    for j in range(1,n-i+1):
        print("*", end="")
    print()

# output
    # *        *
    # **      **
    # ***    ***
    # ****  ****
    # **********
    # ****  ****
    # ***    ***
    # **      **
    # *        *