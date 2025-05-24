# 12. Finding Common Elements: Given two lists, use zip() to find and print common elements.

marks_10th = [78, 90, 67, 56, 89, 99]
marks_12th = [67, 78, 88, 56, 67, 89]

for  tenth, twentieth in zip(marks_10th, marks_12th):
    if tenth == twentieth:
        print("In both class, student got: ", tenth, twentieth)
        break
else:
    print("There is no student who got same marks in both class")
