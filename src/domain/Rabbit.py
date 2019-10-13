class Rabbit:
    def __init__(self):
        self.is_alive = True
        self.age = 0

    def kill(self):
        self.is_alive = False

    def is_dead(self):
        return not self.is_alive

    def can_breed(self):
        return self.age > 3

    def increment_age(self):
        self.age += 1