from src.domain.Coordinate import Coord
from src.domain.World import World
from src.game.CoordGenerator import CoordGenerator


def test_two_rabbits_cant_breed_if_age_less_than_3():
    rabbits_count = 2
    starting_position = [Coord(0, 0), Coord(0, 2)]
    world = World(1, 3, rabbits_count, 0, CoordGenerator(starting_position))

    world.launch_round()

    assert world.territories[1].new_child_rabbit() == 0

