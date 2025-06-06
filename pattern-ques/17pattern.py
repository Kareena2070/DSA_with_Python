
n = 4
for i in range(1, n+1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")

    # Print letters in a pyramid pattern
    char = 65  # ASCII for 'A'
    peak = 2 * i - 1
    for k in range(peak):
        print(chr(char), end="")
        if k < peak // 2:
            char += 1
        else:
            char -= 1
    print()

# output
    #    A
    #   ABA
    #  ABCBA
    # ABCDCBA