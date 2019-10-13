import random

from simulation.domain.Fox import Fox
from simulation.domain.Rabbit import Rabbit
from simulation.domain.World import World
from simulation.game.CoordGenerator import CoordGenerator

max_line = 5
max_column = 5

rabbit_count = 100
fox_count = 100

coord_generator = CoordGenerator(random=True, max_line=max_line, max_colum=max_column)

world = World(max_line, max_column, rabbit_count, fox_count, coord_generator)

print("World instancied with ")
print("foxes : " + str(world.total_fox()))
print("rabbit : " + str(world.total_rabbits()))

print("press enter to start")
input()


while True:

    world.launch_round()

    print("foxes : " + str(world.total_fox()))
    print("rabbit : " + str(world.total_rabbits()))

    print("Do you want to edit eco system ? (y/[n])")
    response = input()

    if response == "y":
        print("How many foxes to add ? [0]")
        foxes_to_add = int(input() or '0')
        for _ in range(foxes_to_add):
            random.choice(world.territories).add_fox(Fox())

        print("How many rabbits to add ? [0]")
        rabbits_to_add = int(input() or '0')
        for _ in range(rabbits_to_add):
            random.choice(world.territories).add_rabbit(Rabbit())

        print("Eco system edited, press Enter to continue")
        input()


