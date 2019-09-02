from src.domain.Breed import Breed
from src.domain.Hunt import Hunt

class Territory():

    def __init__(self):
        self.rabbits = []
        self.foxes   = []
        self.breeded_foxes = 0
        self.breeded_rabbits = 0

    def add_rabbit(self, rabbit):
        self.rabbits += [rabbit]

    def add_fox(self, fox):
        self.foxes += [fox]

    def fox_count(self):
        return len(self.foxes)

    def rabbit_count(self):
        return len(self.rabbits)

    def is_occupied(self):
        return len(self.rabbits) != 0 or len(self.foxes) != 0

    def life_happen(self):
        if len(self.rabbits) == 0:
            self.proceed_foxes()
            pass

        if len(self.foxes) == 0:
            self.proceed_rabbits()
            pass

        self.start_hunt()

    def proceed_foxes(self):
        fed_foxes = self.get_fed_foxes()
        breed = Breed(len(fed_foxes))
        self.breeded_foxes = breed.new_children()

    def get_fed_foxes(self):
        return list(filter(lambda fox: fox.is_fed(), self.foxes))

    def proceed_rabbits(self):
        breed = Breed(len(self.rabbits))
        self.breeded_rabbits = breed.new_children()

    def start_hunt(self):
        hungry_foxes = self.get_hungry_foxes()
        hunt = Hunt(hungry_foxes, self.rabbits)
        hunt.launch()
        self.rabbits = self.get_living_rabbits()

    def get_hungry_foxes(self):
        return list(filter(lambda fox: not fox.is_fed(), self.foxes))

    def get_living_rabbits(self):
        return list(filter(lambda rabbit: not rabbit.is_dead(), self.rabbits))

    def new_child_fox(self):
        return self.breeded_foxes

    def new_child_rabbit(self):
        return self.breeded_rabbits
