from simulation.domain.Coordinate import Coord
from simulation.domain.World import World
from simulation.game.CoordGenerator import CoordGenerator


def test_two_rabbits_cant_breed_if_age_less_than_3():
    rabbits_count = 2
    starting_position = [Coord(0, 0), Coord(0, 2)]
    world = World(1, 3, rabbits_count, 0, CoordGenerator(starting_position))

    world.launch_round()

    assert world.territories[1].new_child_rabbit() == 0


def test_rabbit_should_wait_three_rounds_before_procreating_again():
    rabbits_count = 2
    starting_position = [Coord(0, 0), Coord(0, 0)]
    world = World(1, 2, rabbits_count, 0, CoordGenerator(starting_position))

    for i in range(4):
        world.launch_round()

    assert world.territories[0].rabbit_count() == 3

    world.launch_round()

    assert world.territories[1].rabbit_count() == 3

    world.launch_round()
    world.launch_round()
    world.launch_round()

    assert world.territories[0].rabbit_count() == 4
