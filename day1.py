# Day 1

file = open("input.txt", "r")
elfCals = []
sum = 0

for i in file:
    if len(i.strip()) != 0: 
        sum += int(i)
    else:
        elfCals.append(sum)
        sum = 0

elfCals.sort(reverse= True)
print(elfCals[0]+elfCals[1]+elfCals[2])