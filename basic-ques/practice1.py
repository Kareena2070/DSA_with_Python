# 1. Grade Calculator: Write a program that takes a numerical grade as input and prints the corresponding letter grade (A, B, C, D, F)
# using if-elif-else .

marks = int(input("E`nter your marks: "))

def calGrade(marks):
    if marks>=90:
        print(marks, "Grade A")
    elif marks<=90 and marks>=80:
        print(marks, "Grade B")
    elif marks<=80 and marks >=70:
        print(marks, "Grade C")
    elif marks<=70 and marks>=60:
        print(marks, "Grade D")
    else:
        print(marks, "Grade F")

calGrade(marks)
