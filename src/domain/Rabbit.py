class Rabbit():
    def __init__(self):
        self.is_alive = True

    def kill(self):
        self.is_alive = False

    def is_dead(self):
        return not self.is_alive
