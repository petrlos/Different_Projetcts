#Game of Life

from gamefield import GameField
from gol import GoLstep

size = 6

startField = GameField(size, True)
print(startField)

for _ in range(5):
    startField = GoLstep(startField, size)
    print(startField)