import random


class FoxMovement:
    def __init__(self):
        pass

    @staticmethod
    def next_coord(coords):
        return random.choice(coords)
