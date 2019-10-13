from simulation.domain.Fox import Fox
from simulation.domain.Migration import Migration
from simulation.domain.Rabbit import Rabbit
from simulation.domain.Territory import Territory


def build_territories(total_column, total_line):
    territories = []
    for line in range(total_line):
        territories += [Territory(line, column) for column in range(total_column)]
    return territories


def find_occupied_from(territories):
    return list(filter(lambda t: t.is_occupied(), territories))


def find_foxes(territories):
    return list(filter(lambda t: t.fox_count() != 0, territories))


def find_rabbits(territories):
    return list(filter(lambda t: t.rabbit_count() != 0, territories))


def new_child_rabbit_territories(territories):
    return list(filter(lambda t: t.new_child_rabbit() != 0, territories))


def new_child_fox_territories(territories):
    return list(filter(lambda t: t.new_child_fox() != 0, territories))


def add_new_rabbits_to(territory):
    for _ in range(territory.new_child_rabbit()):
        territory.add_rabbit(Rabbit())

    territory.born_rabbits = 0


def add_new_foxes_to(territory):
    for _ in range(territory.new_child_fox()):
        territory.add_fox(Fox())

    territory.born_foxes = 0


class World:
    def __init__(self, line, column, rabbits, foxes, coord_generator):
        self.round_count = 0
        self.line = line
        self.column = column
        self.territories = build_territories(column, line)
        self.assign_rabbit_to_territories(coord_generator, rabbits)
        self.assign_foxes_to_territories(coord_generator, foxes)

    def assign_foxes_to_territories(self, coord_generator, foxes):
        for fox in range(foxes):
            coord = coord_generator.next_coord()
            list(filter(lambda territory: territory.coord == coord,
                        self.territories))[0].add_fox(Fox())

    def assign_rabbit_to_territories(self, coord_generator, rabbits):
        for rabbit in range(rabbits):
            coord = coord_generator.next_coord()
            list(filter(lambda territory: territory.coord == coord,
                        self.territories))[0].add_rabbit(Rabbit())

    def launch_round(self):
        migration = Migration(self.territories, self.line, self.column)
        migration.migrate_species()

        occupied_territories = find_occupied_from(self.territories)

        [territory.life_happen() for territory in occupied_territories]

        self.rabbit_birth()
        self.fox_birth()

        self.round_count += 1

    def fox_birth(self):
        fox_nests = new_child_fox_territories(self.territories)
        for territory in fox_nests:
            add_new_foxes_to(territory)

    def rabbit_birth(self):
        rabbits_nests = new_child_rabbit_territories(self.territories)
        for territory in rabbits_nests:
            add_new_rabbits_to(territory)

    def total_fox(self):
        foxes_territories = find_foxes(self.territories)
        total = 0
        for territory in foxes_territories:
            total += territory.fox_count()

        return total

    def total_rabbits(self):
        foxes_territories = find_rabbits(self.territories)
        total = 0
        for territory in foxes_territories:
            total += territory.rabbit_count()

        return total
