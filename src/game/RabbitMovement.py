import random


class RabbitMovement:
    def __init__(self):
        pass

    @staticmethod
    def next_coord(coords):
        return random.choice(coords)
