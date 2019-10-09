import unittest

from src.domain.Coordinate import Coord
from src.domain.World import World


class WorldTest(unittest.TestCase):
    def test_fox_should_move_from_one_territory_to_another(self):
        fox_count = 1
        world = World(1, 2, 0, fox_count, MockCoordGenerator())
        world.launch_round()
        assert self.fox_count_for(world, Coord(0, 0)) == 0
        assert self.fox_count_for(world, Coord(0, 1)) == 1

    def test_multiple_fox_should_move_from_one_territory_to_another(self):
        fox_count = 3
        world = World(3, 3, 0, fox_count, MockCoordGenerator())
        world.launch_round()
        assert self.fox_count_for(world, Coord(0, 0)) == 0
        assert self.fox_count_for(world, Coord(2, 2)) == 0
        assert self.fox_count_for(world, Coord(0, 1)) >= 1 or self.fox_count_for(world, Coord(1, 0)) >= 1
        assert self.fox_count_for(world, Coord(1, 2)) == 1 or self.fox_count_for(world, Coord(2, 1)) == 1

    @staticmethod
    def rabbit_count_for(world, coord):
        territories = list(filter(lambda t: t.coord == coord, world.territories))
        assert len(territories) == 1
        return territories[0].rabbit_count()

    @staticmethod
    def fox_count_for(world, coord):
        territories = list(filter(lambda t: t.coord == coord, world.territories))
        assert len(territories) == 1
        return territories[0].fox_count()


class MockCoordGenerator:
    def __init__(self, coord=None):
        if coord is None:
            coord = [Coord(0, 0), Coord(0, 0), Coord(2, 2)]
        self.coord = coord
        self.index = 0

    def next_coord(self):
        coord = self.coord[self.index]
        self.index += 1
        return coord


if __name__ == '__main__':
    unittest.main()
