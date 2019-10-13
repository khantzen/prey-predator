from src.domain.Fox import Fox
from src.domain.Migration import Migration
from src.domain.Rabbit import Rabbit
from src.domain.Territory import Territory


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

        self.round_count += 1

