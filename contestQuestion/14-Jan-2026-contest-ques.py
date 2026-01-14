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


# Winter is Coming
# Chef feels comfortable depending on the temperature and whether or not he is wearing a jacket.

# Chef feels comfortable without a jacket if and only if the temperature is greater than or equal to A.
# Chef feels comfortable with a jacket if and only if the temperature is less than or equal to B.It is guaranteed that A≤BA≤B.
# Chef is not wearing a jacket initially.
# You are given the temperature TiT i​  for the next N days.
# Chef can choose to wear or remove his jacket any number of times, but each time he puts on the jacket is counted as one action.

# Find the minimum number of times Chef needs to wear a jacket so that he feels comfortable on all N days.

# Input Format
# The first line contains a single integer T, denoting the number of test cases.
# For each test case:
# The first line contains three space-separated integers N, A, and B.The second line contains N space-separated integers T1,T2,…,TNT 1​ ,T 2​ ,…,T N​, where TiT i​  is the temperature on the i-th day.
# Output Format
# For each test case, output a single integer — the minimum number of times Chef needs to wear a jacket.

t = int(input("Test case: "))

for _ in range(t):
    n, a, b = list(map(int, input('n, a, b: ').split()))
    t = list(map(int, input("Temperature of everyone: ").split()))
    
    curr_state = 0
    jacket = 0
    
    for temp in t:
        if curr_state == 0 and temp<a:
            curr_state = 1
            jacket+=1
        elif curr_state ==1 and temp >b:
            curr_state =0
            
    print("Minimum number of times Chef wears a jacket is", jacket)