start = 1
for i in range(0, 6):
    if(i%2==0):
        start = 0
    else:
        start = 1
    for j in range(0, i):
        print(start, end="")
        start = 1 - start
    print()

# output
    # 1
    # 01
    # 101
    # 0101
    # 10101