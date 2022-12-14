# day 3 part 2
import numpy as np
pSum = 0
counter = 1
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

file = open("2022/Day3/input.txt", "r")

lines = []
counter = 0
for i in file:
    hash = i.strip()
    lines.append(hash)

for x in range(len(lines)//3):
    fStr = lines[counter]
    sStr = lines[counter+1]
    tStr = lines[counter+2]
    fStrList = list(fStr)
    sStrList = list(sStr)
    tStrList = list(tStr)
    diff = list(set(fStrList) & set(sStrList) & set(tStrList))
    char  = str(diff[0])

    if char.isupper():
        newChar = char.lower()
        priority = alphabet.index(newChar)
        priority += 27
    else:
        priority = alphabet.index(char)
        priority +=1

    pSum += priority

    counter += 3
    print(pSum)
