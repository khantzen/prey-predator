import unittest
from src.game.FoxMovement import FoxMovement
from src.game.Coordonnate import Coord

class FoxMovementTest(unittest.TestCase):
    def test_fox_move_to_random_case(self):
        movement = FoxMovement()
        inputCoord = [Coord(0,0), Coord(2,2), Coord(3,3)]
        nextCase = movement.next(inputCoord)
        assert nextCase in inputCoord
