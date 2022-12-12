# day 3
import numpy as np
pSum = 0
counter = 1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

file = open("2022/Day3/input.txt", "r")

for i in file:
    hash = i.strip()
    lenOfString = len(hash)
    middleOfString = lenOfString
    fPart = i[:middleOfString//2]
    sPart = i[middleOfString//2:lenOfString]
    fPartList = list(fPart)
    sPartList = list(sPart)
    char = np.intersect1d(fPartList, sPartList)
    charStr = np.array2string(char)

    if charStr.isupper():
        newChar = charStr.lower()
        priority = alphabet.index(newChar[2])
        priority += 27
    else:
        priority = alphabet.index(charStr[2])
        priority +=1

    pSum += priority
    print(counter,charStr[2],pSum)
    counter += 1
