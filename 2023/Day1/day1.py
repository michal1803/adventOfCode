# Day 1

file = open("2023/Day1/input.txt", "r")
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digitsList = [{'digit': 'one', 'value': 1},
              {'digit': 'two', 'value': 2},
              {'digit': 'three', 'value': 3},
              {'digit': 'four', 'value': 4},
              {'digit': 'five', 'value': 5},
              {'digit': 'six', 'value': 6},
              {'digit': 'seven', 'value': 7},
              {'digit': 'eight', 'value': 8},
              {'digit': 'nine', 'value': 9}]
sum = 0

    
for i in file:
    for j in digits:
        res = {sub['digit']: sub['value'] for sub in digitsList}
        i.replace(digits[i], str(dict(res)))
    
    arr = []
    for j in i:
        if j.isdigit():
            arr.append(j)

    if len(arr) == 1:
        sum += int(arr[0]+arr[0])
    elif len(arr) > 1:

        sum += int(arr[0]+arr[len(arr)-1])
    print(sum)