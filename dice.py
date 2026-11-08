import random


class Dice:

    def __init__(self, sides: int = 6) -> None:
        """Intialise the dice
        Args:
        sides (int): amount of sides the dice has
        """
        if sides < 2:
            raise ValueError("The die has to have at least two sides")
        self.sides = sides

    def roll(self) -> int:
        """Roll an n-sided dice"""
        self.eyes = random.randint(1, self.sides)
        return self.eyes

    def __repr__(self) -> str:
        """String representation of the dice"""
        return f"Dice(sides={self.sides})"

    def __call__(self) -> int:
        """Calls the roll()-method"""
        return self.roll()
