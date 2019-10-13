from src.domain.Coordinate import Coord
from src.domain.World import World
from src.game.CoordGenerator import CoordGenerator


def test_multiple_rabbit_should_move_from_one_territory_to_another():
    rabbit_count = 3
    world = World(3, 3, rabbit_count, 0, CoordGenerator())
    world.launch_round()
    assert rabbit_count_for(world, Coord(0, 0)) == 0
    assert rabbit_count_for(world, Coord(2, 2)) == 0
    assert rabbit_count_for(world, Coord(0, 1)) >= 1 or rabbit_count_for(world, Coord(1, 0)) >= 1
    assert rabbit_count_for(world, Coord(1, 2)) == 1 or rabbit_count_for(world, Coord(2, 1)) == 1


def test_one_rabbit_should_move_from_one_territory_to_another():
    rabbit_count = 1
    world = World(1, 2, rabbit_count, 0, CoordGenerator())
    world.launch_round()
    assert rabbit_count_for(world, Coord(0, 0)) == 0
    assert rabbit_count_for(world, Coord(0, 1)) == 1


def test_multiple_fox_should_move_from_one_territory_to_another():
    fox_count = 3
    world = World(3, 3, 0, fox_count, CoordGenerator())
    world.launch_round()
    assert fox_count_for(world, Coord(0, 0)) == 0
    assert fox_count_for(world, Coord(2, 2)) == 0
    assert fox_count_for(world, Coord(0, 1)) >= 1 or fox_count_for(world, Coord(1, 0)) >= 1
    assert fox_count_for(world, Coord(1, 2)) == 1 or fox_count_for(world, Coord(2, 1)) == 1


def test_fox_should_move_from_one_territory_to_another():
    fox_count = 1
    world = World(1, 2, 0, fox_count, CoordGenerator())
    world.launch_round()
    assert fox_count_for(world, Coord(0, 0)) == 0
    assert fox_count_for(world, Coord(0, 1)) == 1


def rabbit_count_for(world, coord):
    territories = list(filter(lambda t: t.coord == coord, world.territories))
    assert len(territories) == 1
    return territories[0].rabbit_count()


def fox_count_for(world, coord):
    territories = list(filter(lambda t: t.coord == coord, world.territories))
    assert len(territories) == 1
    return territories[0].fox_count()
