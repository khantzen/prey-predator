class Rabbit:
    def __init__(self):
        self.last_procreation = 0
        self.is_alive = True
        self.age = 0

    def kill(self):
        self.is_alive = False

    def is_dead(self):
        return not self.is_alive

    def can_breed(self):
        return self.age > 3 and self.age - self.last_procreation > 3

    def increment_age(self):
        self.age += 1

    def did_procreate(self):
        self.last_procreation = self.age