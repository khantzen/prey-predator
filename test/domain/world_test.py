import unittest

from src.domain.Coordinate import Coord
from src.domain.World import World


class WorldTest(unittest.TestCase):
    def test_one_world_should_contain_a_dimensionned_grid_of_territory(self):
        line = 10
        column = 10
        world = World(line, column, 0, 0, None)
        assert len(world.territories) == 100

    def test_one_rabbit_start_at_a_random_position(self):
        rabbit_count = 1
        world = World(10, 10, rabbit_count, 0, MockCoordGenerator())
        assert self.rabbit_count_for(world, Coord(0, 0)) == 1
        assert self.rabbit_count_for(world, Coord(4, 4)) == 0

    def test_one_fox_start_at_a_random_position(self):
        fox_count = 1
        world = World(10, 10, 0, fox_count, MockCoordGenerator())
        assert self.fox_count_for(world, Coord(0, 0)) == 1
        assert self.fox_count_for(world, Coord(3, 6)) == 0

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

        assert self.fox_count_for(world, Coord(0, 1)) >= 1 \
               or self.fox_count_for(world, Coord(1, 0)) >= 1

        assert self.fox_count_for(world, Coord(1, 2)) == 1 \
               or self.fox_count_for(world, Coord(2, 1)) == 1

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
    def __init__(self, coord=[Coord(0, 0), Coord(0, 0), Coord(2, 2)]):
        self.coord = coord
        self.index = 0

    def next_coord(self):
        coord = self.coord[self.index]
        self.index += 1
        return coord


if __name__ == '__main__':
    unittest.main()
