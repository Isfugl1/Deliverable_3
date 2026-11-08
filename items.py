from dice import Dice


class Weapon:
    """Represents a weapon a character can hold/equip"""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """initialise the weapon
        Args:
        name (str): what the weapon is called/what kind of weapon it is
        damage_dice (Dice): how much damage the weapon will deal
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Uses the roll()-method from the Dice-class to decide damage"""
        return self.damage_dice.roll()
