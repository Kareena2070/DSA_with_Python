for i in range(1, 6):
    for j in range(1,i):
        print(" ", end="")
    for k in range(0, 2*(6-i)-1):
        print("*", end="")
    print()

# output
    # *********
    #  *******
    #   *****
    #    ***
    #     *