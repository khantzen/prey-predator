from src.domain.Territory import Territory
from src.domain.Rabbit import Rabbit
from src.domain.Fox import Fox
from src.domain.Coordinate import Coord

class World:
    def __init__(self, line, column, rabbits, foxes, coord_generator):
        self.line = line
        self.column = column
        self.grid = [ [Territory() for x in range(column) ] for x in
                     range(line) ]

        for rabbit in range(rabbits):
            coord = coord_generator.next_coord()
            self.grid[coord[0]][coord[1]].add_rabbit(Rabbit())

        for fox in range(foxes):
            coord = coord_generator.next_coord()
            self.grid[coord[0]][coord[1]].add_fox(Fox())
