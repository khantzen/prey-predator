from simulation.domain.Coordinate import Coord
from simulation.domain.World import World
from simulation.game.CoordGenerator import CoordGenerator


def rabbit_count_for(world, coord):
    territories = list(filter(lambda t: t.coord == coord, world.territories))
    assert len(territories) == 1
    return territories[0].rabbit_count()


def fox_count_for(world, coord):
    territories = list(filter(lambda t: t.coord == coord, world.territories))
    assert len(territories) == 1
    return territories[0].fox_count()


def test_one_fox_start_at_a_random_position():
    fox_count = 1
    world = World(10, 10, 0, fox_count, CoordGenerator())
    assert fox_count_for(world, Coord(0, 0)) == 1
    assert fox_count_for(world, Coord(3, 6)) == 0


def test_one_rabbit_start_at_a_random_position():
    rabbit_count = 1
    world = World(10, 10, rabbit_count, 0, CoordGenerator())
    assert rabbit_count_for(world, Coord(0, 0)) == 1
    assert rabbit_count_for(world, Coord(4, 4)) == 0


def test_one_world_should_contain_a_dimensioned_grid_of_territory():
    line = 10
    column = 10
    world = World(line, column, 0, 0, None)
    assert len(world.territories) == 100
