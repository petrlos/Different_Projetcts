#Game of Life
from gamefield import GameField
from copy import deepcopy

def getNeighbourCount(row, column):
    counter = 0
    directions = [(-1,-1), (-1,0), (-1,1), (1,-1), (1,0), (1,1), (0,-1), (0,1)]
    for direction in directions:
        deltaX, deltaY = direction
        neighbourCoords = (row + deltaX, column + deltaY)
        if neighbourCoords in startField.field.keys():
            counter += startField.field[neighbourCoords]
    return counter

size = 6

startField = GameField(size, True)
print(startField)

for _ in range(5):
    newField = GameField(size)
    for row in range(startField.size):
        for column in range(startField.size):
            neighbours = getNeighbourCount(row, column)
            if startField.field[(row, column)] and neighbours in [2,3]:
                newField.field[(row, column)] = 1
            elif not startField.field[(row, column)] and neighbours == 3:
                newField.field[(row, column)] = 1
    startField = deepcopy(newField)
    print(newField)