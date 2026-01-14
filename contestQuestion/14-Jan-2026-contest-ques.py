# Protein Diet
# You consume X grams of protein daily. A balanced diet requires at least Y grams of protein per day.

# Determine whether your daily protein intake fulfills the recommended requirement. The daily protein intake is considered fulfilled if and only if X is greater than or equal to Y.

# Input Format
# The first line of input contains two space-separated integers X and Y - the grams of protein consumed daily and the minimum grams of protein recommended respectively.
# Output Format
# Print YES if the daily protein intake meets or exceeds the recommended amount.
# Otherwise, print NO.

# Each letter of the output may be printed in either uppercase or lowercase, i.e, the strings NO, no, No, and nO will all be treated as equivalent.

x, y = list(map(int, input("Protein consume, Protein requires: ").split()))
if x>=y:
    print("YES")
else:
    print("NO")


