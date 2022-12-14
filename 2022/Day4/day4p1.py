# day 4 part 1

file = open("2022/Day4/input.txt", "r")

counter = 0

for i in file:
    pairs = i.split(",")
    fPair = pairs[0].strip().split("-")
    sPair = pairs[1].strip().split("-")
    ftoListOfNum = list(map(int, fPair))
    stoListOfNum = list(map(int, sPair))

    if ftoListOfNum[0] > stoListOfNum[0]:
        if ftoListOfNum[1] <= stoListOfNum[1]:
            counter += 1
    elif ftoListOfNum[0] == stoListOfNum[0]:
        counter += 1
    else:
        if ftoListOfNum[1] >= stoListOfNum[1]:
            counter += 1
        
    print(ftoListOfNum, stoListOfNum, counter)
