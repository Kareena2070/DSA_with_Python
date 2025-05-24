# 10. Find the First Repeated Character: Given a string, find the first repeated character using a for loop and break

repeatStr = input("Enter you name: ")
seen = []
for i in range(0, len(repeatStr)):
    if repeatStr[i] in seen:
        print("repeated letter is ", repeatStr[i] ,"at index no.: ", i)
        break
    # else:
    #     print("There is no repeadted char")   # if I use else here eveytime when this for run if it not found the repeated char it will print (There is no repeadted char)
    seen.append(repeatStr[i])
else:
    print("There is no reapeated character in this word: ", repeatStr)








    