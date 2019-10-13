from src.domain.Coordinate import Coord
from src.game.FoxMovement import FoxMovement


def test_fox_move_to_random_case():
    movement = FoxMovement()
    input_coord = [Coord(0,0), Coord(2,2), Coord(3,3)]
    next_case = movement.next_coord(input_coord)
    assert next_case in input_coord

