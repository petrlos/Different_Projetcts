#Project Euler - Problem 18
#https://projecteuler.net/problem=18

with open("data.txt") as file:
    lines = file.read().splitlines()

numbers = []
for line in lines:
    numbers.append([int(x) for x in line.split(" ")])

results = []
rows = len(numbers)
for i in range(2 ** (rows - 1)):
    pathIndex = bin(i)[2:]
    path = "0"*(rows-len(pathIndex)) + pathIndex
    checkSum = 0
    rowIndex = 0
    for index, char in enumerate(path):
        rowIndex += int(char)
        checkSum += numbers[index][rowIndex]
    results.append(checkSum)

print("Maximal sum path:",max(results))