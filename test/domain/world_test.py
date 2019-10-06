import unittest
from src.domain.World import World
from src.domain.Territory import Territory
from src.domain.Coordinate import Coord

class WorldTest(unittest.TestCase):

    def test_one_world_should_contain_a_dimensionned_grid_of_territory(self):
        line = 10
        column = 10
        world = World(line, column, 0, 0,  None)
        assert len(world.grid) == 10
        assert len(world.grid[0]) == 10
        assert type(world.grid[0][0]) is Territory

    def test_one_rabbit_start_at_a_random_position(self):
        rabbit_count = 1
        world = World(10, 10, rabbit_count, 0, MockCoordGenerator())
        assert world.grid[0][0].rabbit_count() == 1
        assert world.grid[4][4].rabbit_count() == 0

    def test_one_fox_start_at_a_random_position(self):
        fox_count = 1
        world = World(10, 10, 0, fox_count, MockCoordGenerator())
        assert world.grid[0][0].fox_count() == 1
        assert world.grid[3][6].fox_count() == 0


class MockCoordGenerator():
    def __init__(self):
        self.coord = [[0,0], [0,0], [2,2]]
        self.index = 0

    def next_coord(self):
        coord = self.coord[self.index]
        self.index += 1
        return coord

if __name__ == '__main__':
    unittest.main()
