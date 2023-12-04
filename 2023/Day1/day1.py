# Day 1

file = open("2023/Day1/input.txt", "r")

sum = 0

for i in file:
    arr = []
    for j in i:
        if j.isdigit():
            arr.append(j)

    if len(arr) == 1:
        sum += int(arr[0]+arr[0])
    elif len(arr) > 1:

        sum += int(arr[0]+arr[len(arr)-1])
    print(sum)