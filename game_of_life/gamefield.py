class GameField:
    def __init__(self, size, readFromFile=False):
        self.size = size
        self.field = {}
        for row in range(size):
            for column in range(size):
                self.field[(row, column)] = 0
        if readFromFile:
            self.__readFromFile()

    def __str__(self):
        description = ""
        for row in range(self.size):
            for column in range(self.size):
                if (row, column) in self.field.keys():
                    description += "#" if self.field[(row, column)] else "."
                description += " "
            description += "\n"
        return description

    def __readFromFile(self):
        with open("text.txt") as file:
            lines = file.read().splitlines()
        for row, line in enumerate(lines):
            for column, char in enumerate(line):
                if char == "1":
                    self.field[(row, column)] = 1
                else:
                    self.field[(row, column)] = 0