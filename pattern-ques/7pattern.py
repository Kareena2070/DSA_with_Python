for i in range(1, 6):
    for j in range(1,  6-i):
        print(" ", end="")
    for k in range(0, 2*i-1):
        print("*", end="")
    for l in range(1, 6-i):         # This loop can be remove. if if remove then also pattern show same pattern
        print(" ", end="")
    print()

# output
    #     *    
    #    ***   
    #   *****  
    #  ******* 
    # *********