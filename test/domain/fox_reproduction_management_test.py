from src.domain.Coordinate import Coord
from src.domain.World import World
from src.game.CoordGenerator import CoordGenerator


def test_two_fed_fox_met_territory_should_breed_one_fox():
    world = two_fox_simulation()
    assert world.territories[1].fox_count() == 3


def test_one_fed_and_one_hungry_fox_should_breed_no_child():
    fox_count = 2
    starting_position = [Coord(0, 0), Coord(0, 2)]
    world = World(1, 3, 0, fox_count, CoordGenerator(starting_position))

    world.territories[0].foxes[0].feed()

    world.launch_round()

    assert world.territories[1].fox_count() == 2


def test_fox_should_be_hungry_after_breeding():
    world = two_fox_simulation()
    assert not world.territories[1].foxes[0].is_fed()
    assert not world.territories[1].foxes[1].is_fed()


def two_fox_simulation():
    fox_count = 2
    starting_position = [Coord(0, 0), Coord(0, 2)]
    world = World(1, 3, 0, fox_count, CoordGenerator(starting_position))
    world.territories[0].foxes[0].feed()
    world.territories[2].foxes[0].feed()
    world.launch_round()
    return world
