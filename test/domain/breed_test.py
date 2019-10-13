from simulation.domain.Breed import Breed


def test_one_couple_should_breed_1_child():
    breed = Breed(2)
    assert breed.new_children() == 1


def test_4_units_should_breed_2_children():
    breed = Breed(4)
    assert breed.new_children() == 2


def test_5_units_should_breed_2_children():
    breed = Breed(5)
    assert breed.new_children() == 2
