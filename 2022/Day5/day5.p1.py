# day 5 part 1
import numpy as np


file = open("2022/Day5/matrix.txt", "r")
order = open("2022/Day5/input.txt", "r")

#reverse list idea 
for line in reversed(list(file)):
    print(line.rstrip())
