from src.domain.Fox import Fox
from src.domain.Rabbit import Rabbit
from src.domain.Territory import Territory
from src.game.FoxMovement import FoxMovement
from src.game.RabbitMovement import RabbitMovement


class World:
    def __init__(self, line, column, rabbits, foxes, coord_generator):
        self.round_count = 0
        self.line = line
        self.column = column
        self.territories = []

        self.build_territories(column, line)

        for rabbit in range(rabbits):
            coord = coord_generator.next_coord()
            list(filter(lambda territory: territory.coord == coord,
                        self.territories))[0].add_rabbit(Rabbit())

        for fox in range(foxes):
            coord = coord_generator.next_coord()
            list(filter(lambda territory: territory.coord == coord,
                        self.territories))[0].add_fox(Fox())

    def build_territories(self, column, line):
        for l in range(line):
            for c in range(column):
                self.territories += [Territory(l, c)]

    def launch_round(self):
        occupied_territories = self.find_occupied()
        fox_territories = self.find_foxes(occupied_territories)
        rabbit_territories = self.find_rabbits(occupied_territories)

        for territory in fox_territories:
            self.foxes_migrate_from(territory)

        for territory in rabbit_territories:
            self.rabbits_migrate_from(territory)

        occupied_territories = self.find_occupied()

        for territory in occupied_territories:
            territory.life_happen()

        self.round_count += 1

    def foxes_migrate_from(self, territory):
        adj = territory.coord.adjacent(self.line, self.column)

        while territory.fox_count() != 0:
            fox = territory.remove_one_fox()

            if fox.is_not_dead_from_hunger():
                coord = self.next_coord(adj, FoxMovement())
                self.add_fox_to(coord, fox)

    def rabbits_migrate_from(self, territory):
        adj = territory.coord.adjacent(self.line, self.column)

        while territory.rabbit_count() != 0:
            rabbit = territory.remove_one_rabbit()
            coord = self.next_coord(adj, RabbitMovement())
            self.add_rabbit_to(coord, rabbit)

    def find_occupied(self):
        return list(filter(lambda t: t.is_occupied(), self.territories))

    def add_fox_to(self, coord, fox):
        list(filter(lambda territory: territory.coord == coord,
                    self.territories))[0].add_fox(fox)

    def add_rabbit_to(self, coord, rabbit):
        list(filter(lambda territory: territory.coord == coord,
                    self.territories))[0].add_rabbit(rabbit)

    @staticmethod
    def next_coord(adj, move):
        coord = move.next_coord(adj)
        return coord

    @staticmethod
    def find_foxes(territories):
        return list(filter(lambda t: t.fox_count() != 0, territories))

    @staticmethod
    def find_rabbits(territories):
        return list(filter(lambda t: t.rabbit_count() != 0, territories))