class Fox:
    def __init__(self):
        self.is_hungry = True
        self.age = 0
        self.last_meal = 0

    def feed(self):
        self.is_hungry = False
        self.last_meal = self.age

    def is_fed(self):
        return not self.is_hungry

    def increment_age(self):
        self.age += 1

    def is_not_dead_from_hunger(self):
        return self.age - self.last_meal < 5
