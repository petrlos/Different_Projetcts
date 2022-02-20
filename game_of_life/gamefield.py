class GameField:
    def __init__(self):
        self.size = 0
        self.field = {}

    def __str__(self):
        description = ""
        for row in range(self.size):
            for column in range(self.size):
                if (row, column) in self.field.keys():
                    description += self.field[(row, column)]
                else:
                    description += "."
                description += " "
            description += "\n"
        return description

    def readFromFile(self):
        with open("text.txt") as file:
            lines = file.read().splitlines()
        for row, line in enumerate(lines):
            for column, char in enumerate(line):
                if char == "1":
                    self.field[(row, column)] = "#"
        self.size = row + 1