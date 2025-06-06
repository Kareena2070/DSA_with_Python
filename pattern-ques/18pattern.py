n = 5
for i in range(0, n):
    for j in range(n-i, n+1): # j from (5-i) to 5
        print(chr(64+j), end="")
    print()

# output
    # E
    # DE
    # CDE
    # BCDE
    # ABCDE