import random

class FoxMovement():
    def __init__(self):
        pass

    def next(self, coords):
        return random.choice(coords)
