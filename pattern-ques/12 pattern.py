for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    for k in range(0, 2*(4-i)):
        print(" ", end="")
    for j in range(i, 0, -1):     # for reverse the number we use 3 condition in range(start, stopt, step) just like in JS we give i=0 to start, i<10 to stop, i++ to step
        print(j, end="")
    print()

# output
    # 1      1
    # 12    21
    # 123  321
    # 12344321