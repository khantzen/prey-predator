from simulation.domain.Coordinate import Coord
import random


class CoordGenerator:
    def __init__(self, coord=None, random=False, max_line=0, max_colum=0):
        if coord is None and not random:
            coord = [Coord(0, 0), Coord(0, 0), Coord(2, 2)]
        self.coord = coord
        self.index = 0
        self.random = random
        self.max_line = max_line
        self.max_column = max_colum

    def next_coord(self):
        if self.random:
            return Coord(random.choice(range(self.max_line)), random.choice(range(self.max_column)))

        coord = self.coord[self.index]
        self.index += 1
        return coord
