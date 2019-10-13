from src.domain.Fox import Fox
from src.domain.Hunt import Hunt
from src.domain.Rabbit import Rabbit


def test_rabbit_should_be_eaten_when_met_one_fox():
    fox = Fox()
    rabbit = Rabbit()
    hunt = Hunt([fox], [rabbit])
    hunt.launch()
    assert fox.is_fed()
    assert rabbit.is_dead()


def test_two_rabbit_met_one_fox_one_is_eaten_the_other_survive():
    fox = Fox()
    rabbit_1 = Rabbit()
    rabbit_2 = Rabbit()
    hunt = Hunt([fox], [rabbit_1, rabbit_2])
    hunt.launch()
    assert fox.is_fed()
    assert rabbit_1.is_dead()
    assert not rabbit_2.is_dead()


def test_two_foxes_met_one_rabbit_only_one_fox_should_be_fed():
    fox_1 = Fox()
    fox_2 = Fox()
    rabbit = Rabbit()
    hunt = Hunt([fox_1, fox_2], [rabbit])
    hunt.launch()
    assert fox_1.is_fed()
    assert not fox_2.is_fed()
    assert rabbit.is_dead()
