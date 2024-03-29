from simulation.domain.Fox import Fox
from simulation.domain.Rabbit import Rabbit
from simulation.domain.Territory import Territory


def test_add_one_rabbit_to_territory():
    rabbit = Rabbit()
    territory = Territory()
    territory.add_rabbit(rabbit)
    assert territory.rabbit_count() == 1
    assert territory.is_occupied()


def test_add_two_rabbits_to_territory():
    territory = Territory()
    territory.add_rabbit(Rabbit())
    territory.add_rabbit(Rabbit())
    assert territory.rabbit_count() == 2


def test_add_one_fox_to_territory():
    territory = Territory()
    territory.add_fox(Fox())
    assert territory.fox_count() == 1
    assert territory.is_occupied()


def test_add_two_fox_to_territory():
    territory = Territory()
    territory.add_fox(Fox())
    territory.add_fox(Fox())
    assert territory.fox_count() == 2
    assert territory.is_occupied()


def test_new_territory_shouldnt_be_occupied():
    territory = Territory()
    assert not territory.is_occupied()


def test_5_rabbits_and_5_hungry_fox_should_left_no_rabbit_alive():
    territory = Territory()
    for i in range(5):
        territory.add_rabbit(Rabbit())
        territory.add_fox(Fox())

    territory.life_happen()
    assert territory.rabbit_count() == 0


def test_5_rabbits_and_no_fox_should_breed_no_rabbit_when_life_happen():
    territory = Territory()
    for i in range(5):
        rabbit = Rabbit()
        rabbit.age = 5
        territory.add_rabbit(rabbit)

    territory.life_happen()
    assert territory.new_child_rabbit() == 2


def test_5_fed_fox_and_one_hungry_and_no_rabbit_should_breed_2_fox():
    territory = Territory()
    for i in range(5):
        territory.add_fox(fed_fox())

    territory.add_fox(Fox())
    territory.life_happen()
    assert territory.new_child_fox() == 2


def test_2_fed_fox_and_no_rabbit_should_breed_1_child_fox():
    fox_1 = fed_fox()
    fox_2 = fed_fox()
    territory = Territory()
    territory.add_fox(fox_1)
    territory.add_fox(fox_2)
    territory.life_happen()
    assert territory.new_child_fox() == 1


def fed_fox():
    fox = Fox()
    fox.feed()
    return fox
