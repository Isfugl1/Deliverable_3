import random


class Dice:

    def __init__(self, sides: int = 6):
        if sides < 2:
            raise ValueError("The die has to have at least two sides")
        self.sides = sides

    def roll(self):
        self.eyes = random.randint(1, self.sides)
        return self.eyes

    def __repr__(self):
        return f"Dice(sides={self.sides})"

    def __call__(self):
        # self.eyes = self.roll()
        return self.roll()
