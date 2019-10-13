import unittest
from simulation.game.RabbitMovement import RabbitMovement
from simulation.domain.Coordinate import Coord


def test_rabbit_move_to_random_case():
    movement = RabbitMovement()
    input_coord = [Coord(0,0), Coord(1,1), Coord(7,23)]
    next_case = movement.next_coord(input_coord)
    assert next_case in input_coord
