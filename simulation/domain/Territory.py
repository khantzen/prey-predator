from simulation.domain.Breed import Breed
from simulation.domain.Hunt import Hunt
from simulation.domain.Coordinate import Coord


class Territory:
    def __init__(self, line=0, column=0):
        self.rabbits = []
        self.temp_rabbit = []
        self.foxes = []
        self.temp_fox = []
        self.born_foxes = 0
        self.born_rabbits = 0
        self.coord = Coord(line, column)

    def add_rabbit(self, rabbit):
        self.rabbits += [rabbit]

    def add_new_rabbit(self, rabbit):
        self.temp_rabbit += [rabbit]

    def add_fox(self, fox):
        self.foxes += [fox]

    def add_new_fox(self, fox):
        self.temp_fox += [fox]

    def end_migration(self):
        self.rabbits = self.temp_rabbit
        self.foxes = self.temp_fox
        self.temp_rabbit = []
        self.temp_fox = []

    def remove_one_fox(self):
        fox = self.foxes[0]
        self.foxes = self.foxes[1::]
        fox.increment_age()
        return fox

    def remove_one_rabbit(self):
        rabbit = self.rabbits[0]
        self.rabbits = self.rabbits[1::]
        return rabbit

    def fox_count(self):
        return len(self.foxes)

    def rabbit_count(self):
        return len(self.rabbits)

    def is_occupied(self):
        return len(self.rabbits) != 0 or len(self.foxes) != 0

    def life_happen(self):
        self.start_hunt()
        self.proceed_foxes()
        self.proceed_rabbits()

    def proceed_foxes(self):
        self.born_foxes = 0
        fed_foxes = self.get_fed_foxes()
        breed = Breed(len(fed_foxes))
        self.born_foxes = breed.new_children()
        for x in range(self.born_foxes * 2):
            fed_foxes[x].had_breed()

    def get_fed_foxes(self):
        return list(filter(lambda fox: fox.can_breed(), self.foxes))

    def proceed_rabbits(self):
        self.born_rabbits = 0
        mature_rabbits = self.get_mature_rabbits()
        breed = Breed(len(mature_rabbits))
        self.born_rabbits = breed.new_children()
        [rabbit.did_procreate() for rabbit in mature_rabbits]

    def start_hunt(self):
        hungry_foxes = self.get_hungry_foxes()
        hunt = Hunt(hungry_foxes, self.rabbits)
        hunt.launch()
        self.rabbits = self.get_living_rabbits()

    def get_hungry_foxes(self):
        return list(filter(lambda fox: not fox.is_fed(), self.foxes))

    def get_mature_rabbits(self):
        return list(filter(lambda rabbit: rabbit.can_breed(), self.rabbits))

    def get_living_rabbits(self):
        return list(filter(lambda rabbit: not rabbit.is_dead(), self.rabbits))

    def new_child_fox(self):
        return self.born_foxes

    def new_child_rabbit(self):
        return self.born_rabbits

    def adjacent(self, max_line, max_column):
        return self.coord.adjacent(max_line, max_column)