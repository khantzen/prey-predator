from src.domain.Coordinate import Coord
from src.domain.World import World


def test_two_fed_fox_met_territory_should_breed_one_fox():
    world = two_fox_simulation()
    assert world.territories[1].new_child_fox() == 1


def test_one_fed_and_one_hungry_fox_should_breed_no_child():
    fox_count = 2
    starting_position = [Coord(0, 0), Coord(0, 2)]
    world = World(1, 3, 0, fox_count, MockCoordGenerator(starting_position))

    world.territories[0].foxes[0].feed()

    world.launch_round()

    assert world.territories[1].new_child_fox() == 0


def test_fox_should_be_hungry_after_breeding():
    world = two_fox_simulation()
    assert not world.territories[1].foxes[0].is_fed()
    assert not world.territories[1].foxes[1].is_fed()


def two_fox_simulation():
    fox_count = 2
    starting_position = [Coord(0, 0), Coord(0, 2)]
    world = World(1, 3, 0, fox_count, MockCoordGenerator(starting_position))
    world.territories[0].foxes[0].feed()
    world.territories[2].foxes[0].feed()
    world.launch_round()
    return world


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
