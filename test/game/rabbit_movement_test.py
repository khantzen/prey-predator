import unittest
from src.game.RabbitMovement import RabbitMovement
from src.game.Coordonnate import Coord

class RabbitMovementTest(unittest.TestCase):
    def test_rabbit_move_to_random_case(self):
        movement = RabbitMovement()
        inputCoord = [Coord(0,0), Coord(1,1), Coord(7,23)]
        nextCase = movement.next(inputCoord)
        assert nextCase in inputCoord
