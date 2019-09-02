import unittest
from src.domain.Breed import Breed

class BreedTest(unittest.TestCase):
    def test_one_couple_should_breed_1_child(self):
        breed = Breed(2)
        assert breed.new_children() == 1

    def test_4_units_should_breed_2_children(self):
        breed = Breed(4)
        assert breed.new_children() == 2

    def test_5_units_should_breed_2_children(self):
        breed = Breed(5)
        assert breed.new_children() == 2

if __name__ == '__main__':
    unittest.main()
