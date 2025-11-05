# Fuel Check
# Chef plans to go on a long drive, and is now checking whether he has enough fuel for the trip.
# Chef's car has X units of fuel remaining.
# The car has a fuel efficiency of Y, meaning that for each unit of fuel it has, it can travel a distance of Y kilometers.

# Chef knows that the distance he needs to travel is exactly 100 kilometers.
# Does he have enough fuel for his trip?

# Input Format
# The only line of input will contain three space-separated integers 
# X and Y — the amount of fuel remaining and the car's fuel efficiency, respectively.
# Output Format
# For each test case, output on a new line the answer: Yes if Chef has enough fuel remaining, and No otherwise.
# Each character of the output can be printed in either uppercase or lowercase, i.e. the strings NO, no, No, and nO will all be treated as equivalent.

# Sample 1:
# Input
# 1 100
# Output
# Yes
# Explanation
# Chef has 1 unit of fuel, and the car can travel 100 kilometers with that fuel.  

x, y = list(map(int, input().split()))

if (x*y) >= 100:
    print("Yes")
else:
    print("No")

