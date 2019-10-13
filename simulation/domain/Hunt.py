class Hunt:
    def __init__(self, foxes, rabbits):
        self.foxes = foxes
        self.rabbits = rabbits

    def launch(self):
        for fox, rabbit in zip(self.foxes, self.rabbits):
            rabbit.kill()
            fox.feed()
