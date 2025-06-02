for i in range(1, 6):
    for j in range(1,6-i+1):
        print(chr(64+j), end="")
    print()

# output
    # ABCDE
    # ABCD
    # ABC
    # AB
    # A