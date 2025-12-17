# Playing with Toys
# Chef got N toys for his birthday. Everyday, if he has at least one toy with him, he plays with one specific toy for that day.

# Unfortunately, Chef is very careless, and will inevitably break that toy by the end of the day. When he does break it, he does not play with a new toy but just waits for the next day.

# After M days, how many toys will Chef be left with?

# Example usage:
# Input:
# 5 2
# Output:
# 3

n,m = list(map(int, input("number toys and number of days: ").split()))

k = n-m
if k < 0:
    print(0)
else:
    print(k)




