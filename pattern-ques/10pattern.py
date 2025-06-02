for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end="")
    print()
for k in range(1, 5):
    for l in range(1, 5-k+1):
        print("*", end="")
    print()

# output
    # *
    # **
    # ***
    # ****
    # *****
    # ****
    # ***
    # **
    # *