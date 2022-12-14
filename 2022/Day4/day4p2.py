# day 4 part 2

file = open("2022/Day4/input.txt", "r")

counter = 0
fileSize = 0

for i in file:
    fileSize += 1
    pairs = i.split(",")
    fPair = pairs[0].strip().split("-")
    sPair = pairs[1].strip().split("-")
    ftoListOfNum = list(map(int, fPair))
    stoListOfNum = list(map(int, sPair))

    # Trying to find pairs of numbers that dont ovelap
    # Then substract those pairs from all pairs in file
    if ftoListOfNum[0] > stoListOfNum[0]:
        if ftoListOfNum[0] > stoListOfNum[1]:
            counter += 1
    elif ftoListOfNum[0] < stoListOfNum[0]:
        if ftoListOfNum[1] < stoListOfNum[0]:
            counter += 1
    

    print(ftoListOfNum, stoListOfNum, counter,fileSize-counter)
