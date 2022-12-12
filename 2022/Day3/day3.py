# day 3

file = open("2022/Day3/input.txt", "r")

for i in file:
    lenOfString = len(i)
    middleOfString = lenOfString/2
    fPart =i[0:middleOfString]
    sPart =i[middleOfString:lenOfString]
    print(fPart + "   " + sPart)