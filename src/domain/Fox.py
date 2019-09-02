class Fox():
    def __init__(self):
        self.is_hungry = True

    def feed(self):
        self.is_hungry = False

    def is_fed(self):
        return not self.is_hungry
