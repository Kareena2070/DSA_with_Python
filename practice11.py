# 11. Multiplication Table: Generate a multiplication table from 1 to 10 using nested loops.

num = int(input("Enter a number which multiplication you want: "))

for j in range(1, 11):
        mult = j*num
        print(num,"*",j, "=",mult)


for i in range(1, 11):
        for j in range(1, 11):
                print(i*j, end=" ")
        print()
        