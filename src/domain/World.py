from src.domain.Fox import Fox
from src.domain.Rabbit import Rabbit
from src.domain.Territory import Territory
from src.game.FoxMovement import FoxMovement


class World:
    def __init__(self, line, column, rabbits, foxes, coord_generator):
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

        print(str(len(fox_territories)))

        for territory in fox_territories:
            print(str(territory.fox_count()))
            self.move_foxes(territory)

    def move_foxes(self, territory):
        adj = territory.coord.adjacent(self.line, self.column)

        while territory.fox_count() != 0:
            fox = territory.remove_one_fox()
            move = FoxMovement()
            coord = move.next_coord(adj)
            self.add_fox_to(coord, fox)

    def find_occupied(self):
        return list(filter(lambda t: t.is_occupied(), self.territories))

    def add_fox_to(self, coord, fox):
        list(filter(lambda territory: territory.coord == coord,
                    self.territories))[0].add_fox(fox)

    @staticmethod
    def find_foxes(territories):
        return list(filter(lambda t: t.fox_count() != 0, territories))
