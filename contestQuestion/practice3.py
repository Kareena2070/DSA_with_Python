# 

t = int(input("Number of test case: "))

for i in range(t):
    a, b = list(map(int, input("Number of episodes and time: ").split()))
    x = a * b 
    if x < 60:
        print(0, x)
    elif x == 60:
        print(1, 0)
    else:
        y = x//60
        print(y,"hr", x-(y*60),"m")