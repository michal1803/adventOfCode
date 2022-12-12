# day 2

file = open("2022/Day2/input.txt", "r")

rock = 1  # A or X
paper = 2  # B or Y
scissors = 3  # C or Z
score = 0
index = 0


def challange(h, m):
    score = 0
    match h:
        case "A":  # rock
            if m == "Y":
                score += 4  
            elif m == "X":
                score += 3  
            elif m == "Z":
                score += 8  
        case "B":  # paper
            if m == "X":
                score += 1
            elif m == "Y":
                score += 5
            elif m == "Z":
                score += 9
        case "C":  # scissors
            if m == "Z":
                score += 7
            elif m == "X":
                score += 2
            elif m == "Y":
                score += 6
    return score


for i in file:
    listOfRow = list(i)
    score = score + challange(listOfRow[0], listOfRow[2])
    index += 1
    print("index: " + str(index) + " score: " + str(score))
