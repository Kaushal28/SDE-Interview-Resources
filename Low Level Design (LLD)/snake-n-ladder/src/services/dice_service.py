import random


class DiceService:
    """Dice service that helps to roll the dice."""

    @staticmethod
    def roll():
        return random.randint(1, 6)
