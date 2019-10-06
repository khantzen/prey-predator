import unittest
from src.domain.Coordinate import Coord

class CoordinateTest(unittest.TestCase):
    def test_get_available_case_at_center(self):
        adjacentCases = Coord(5,5).adjacents(10, 10)
        assert len(adjacentCases) == 4
        assert Coord(4,5) in adjacentCases
        assert Coord(6,5) in adjacentCases
        assert Coord(5,6) in adjacentCases
        assert Coord(5,4) in adjacentCases

    def test_available_case_at_right_bottom_corner(self):
        adjacentCases = Coord(9,9).adjacents(10,10)
        assert len(adjacentCases) == 2
        assert Coord(8,9) in adjacentCases
        assert Coord(9,8) in adjacentCases

    def test_available_case_at_left_bottom_corner(self):
        adjacentCases = Coord(9,0).adjacents(10,10)
        assert len(adjacentCases) == 2
        assert Coord(8,0) in adjacentCases
        assert Coord(9,1) in adjacentCases

    def test_availables_case_at_right_top_corner(self):
        adjacentCases = Coord(0,9).adjacents(10,10)
        assert len(adjacentCases) == 2
        assert Coord(0,8) in adjacentCases
        assert Coord(1,9) in adjacentCases

    def test_availabe_case_at_non_corner_edge(self):
        adjacentCases = Coord(5,9).adjacents(10,10)
        assert len(adjacentCases) == 3
        assert Coord(5,8) in adjacentCases
        assert Coord(4,9) in adjacentCases
        assert Coord(6,9) in adjacentCases

if __name__ == '__main__':
    unittest.main()
