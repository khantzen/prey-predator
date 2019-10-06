class Coord():
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def __eq__(self, target):
        return self.line == target.line and self.column == target.column
