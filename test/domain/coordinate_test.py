import unittest
from src.domain.Coordinate import Coord


class CoordinateTest(unittest.TestCase):
    def test_get_available_case_at_center(self):
        adjacent_cases = Coord(5, 5).adjacent(10, 10)
        assert len(adjacent_cases) == 4
        assert Coord(4, 5) in adjacent_cases
        assert Coord(6, 5) in adjacent_cases
        assert Coord(5, 6) in adjacent_cases
        assert Coord(5, 4) in adjacent_cases

    def test_available_case_at_right_bottom_corner(self):
        adjacent_cases = Coord(9, 9).adjacent(10, 10)
        assert len(adjacent_cases) == 2
        assert Coord(8, 9) in adjacent_cases
        assert Coord(9, 8) in adjacent_cases

    def test_available_case_at_left_bottom_corner(self):
        adjacent_cases = Coord(9, 0).adjacent(10, 10)
        assert len(adjacent_cases) == 2
        assert Coord(8, 0) in adjacent_cases
        assert Coord(9, 1) in adjacent_cases

    def test_availables_case_at_right_top_corner(self):
        adjacent_cases = Coord(0, 9).adjacent(10, 10)
        assert len(adjacent_cases) == 2
        assert Coord(0, 8) in adjacent_cases
        assert Coord(1, 9) in adjacent_cases

    def test_availabe_case_at_non_corner_edge(self):
        adjacent_cases = Coord(5, 9).adjacent(10, 10)
        assert len(adjacent_cases) == 3
        assert Coord(5, 8) in adjacent_cases
        assert Coord(4, 9) in adjacent_cases
        assert Coord(6, 9) in adjacent_cases


if __name__ == '__main__':
    unittest.main()
