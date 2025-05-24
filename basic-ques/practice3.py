# 3. Leap Year Checker: Check if a given year is a leap year using nested conditionals.

year = int(input("Enter year to know its leap year or not: "))

def leapYear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        print(year, "is Leap year")
    else:
        print(year, "not a Leap year")
leapYear(year)