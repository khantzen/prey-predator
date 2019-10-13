from src.game.FoxMovement import FoxMovement
from src.game.RabbitMovement import RabbitMovement


def find_occupied_from(territories):
    return list(filter(lambda t: t.is_occupied(), territories))


def find_foxes(territories):
    return list(filter(lambda t: t.fox_count() != 0, territories))


def find_rabbits(territories):
    return list(filter(lambda t: t.rabbit_count() != 0, territories))


def next_coord(adj, move):
    coord = move.next_coord(adj)
    return coord


def add_rabbit_to(coord, territories, rabbit):
    list(filter(lambda territory: territory.coord == coord,
                territories))[0].add_new_rabbit(rabbit)


def add_fox_to(coord, territories, fox):
    list(filter(lambda territory: territory.coord == coord,
                territories))[0].add_new_fox(fox)


class Migration:
    def __init__(self, territories, max_line, max_column):
        self.territories = territories
        self.max_line = max_line
        self.max_column = max_column

    def migrate_species(self):
        occupied_territories = find_occupied_from(self.territories)

        fox_territories = find_foxes(occupied_territories)
        self.migrate_foxes(fox_territories)

        rabbit_territories = find_rabbits(occupied_territories)
        self.migrate_rabbits(rabbit_territories)

        [territory.end_migration() for territory in self.territories]

    def migrate_foxes(self, fox_territories):
        [self.migrate(territory, self.move_fox) for territory in fox_territories]

    def migrate_rabbits(self, rabbit_territories):
        [self.migrate(territory, self.move_rabbit) for territory in rabbit_territories]

    def migrate(self, territory, specie_migration):
        adj = territory.adjacent(self.max_line, self.max_column)
        specie_migration(adj, territory)

    def move_fox(self, adj, territory):
        while territory.fox_count() != 0:
            fox = territory.remove_one_fox()

            if fox.is_not_dead_from_hunger():
                coord = next_coord(adj, FoxMovement())
                add_fox_to(coord, self.territories, fox)

    def move_rabbit(self, adj, territory):
        while territory.rabbit_count() != 0:
            rabbit = territory.remove_one_rabbit()
            rabbit.increment_age()
            coord = next_coord(adj, RabbitMovement())
            add_rabbit_to(coord, self.territories, rabbit)
