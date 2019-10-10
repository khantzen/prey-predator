import unittest

from src.domain.Coordinate import Coord
from src.domain.World import World


class WorldTest(unittest.TestCase):
    def test_fox_should_die_from_hunger_after_5_rounds_without_being_fed(self):
        fox_count = 1
        world = World(1, 2, 0, fox_count, MockCoordGenerator())

        for x in range(6):
            world.launch_round()

        assert world.territories[0].fox_count() == 0

    def test_fox_should_stay_alive_if_feed_during_the_last_five_turn(self):
        fox_count = 1
        world = World(1, 2, 0, fox_count, MockCoordGenerator())

        for x in range(4):
            world.launch_round()

        world.territories[0].foxes[0].feed()

        for x in range(2):
            world.launch_round()

        assert world.territories[0].fox_count() == 1

    def test_fox_should_be_hungry_if_not_feed_during_last_three_turn(self):
        fox_count = 1
        world = World(1, 2, 0, fox_count, MockCoordGenerator())

        for x in range(4):
            world.launch_round()

        world.territories[0].foxes[0].feed()

        for x in range(4):
            world.launch_round()

        assert not world.territories[0].foxes[0].is_fed()


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
