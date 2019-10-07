class Coord():
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def adjacent(self, line_max, column_max):
        adjacent_coords = []

        if self.has_valid_top_case():
            adjacent_coords += [self.top_case()]

        if self.has_valid_left_case():
            adjacent_coords += [self.left_case()]

        if self.has_valid_right_case(column_max):
            adjacent_coords += [self.right_case()]

        if self.has_valid_bottom_case(line_max):
            adjacent_coords += [self.bottom_case()]

        return adjacent_coords

    def has_valid_top_case(self):
        return self.line - 1 >= 0

    def top_case(self):
        return Coord(self.line - 1, self.column)

    def has_valid_left_case(self):
        return self.column - 1 >= 0

    def left_case(self):
        return Coord(self.line, self.column - 1)

    def has_valid_right_case(self, column_max):
        return self.column + 1 < column_max

    def right_case(self):
        return Coord(self.line, self.column + 1)

    def has_valid_bottom_case(self, line_max):
        return self.line + 1 < line_max

    def bottom_case(self):
        return Coord(self.line + 1, self.column)

    def __eq__(self, target):
        return self.line == target.line and self.column == target.column

    def __str__(self):
        return "Coord line:" + str(self.line) + " | col: " + str(self.column)
