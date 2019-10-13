from simulation.domain.World import World
from simulation.game.CoordGenerator import CoordGenerator


def test_fox_should_die_from_hunger_after_5_rounds_without_being_fed():
    fox_count = 1
    world = World(1, 2, 0, fox_count, CoordGenerator())

    for x in range(6):
        world.launch_round()

    assert world.territories[0].fox_count() == 0


def test_fox_should_stay_alive_if_feed_during_the_last_five_turn():
    fox_count = 1
    world = World(1, 2, 0, fox_count, CoordGenerator())

    for x in range(4):
        world.launch_round()

    world.territories[0].foxes[0].feed()

    for x in range(2):
        world.launch_round()

    assert world.territories[0].fox_count() == 1


def test_fox_should_be_hungry_if_not_feed_during_last_three_turn():
    fox_count = 1
    world = World(1, 2, 0, fox_count, CoordGenerator())

    for x in range(4):
        world.launch_round()

    world.territories[0].foxes[0].feed()

    for x in range(4):
        world.launch_round()

    assert not world.territories[0].foxes[0].is_fed()

