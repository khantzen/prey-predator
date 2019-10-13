class Breed:
    def __init__(self, unit_count):
        self.unit_count = unit_count

    def new_children(self):
        return int(self.unit_count / 2)
