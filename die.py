from random import randint


class Die:
    """A six-sided die."""

    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    def roll(self):
        """Randomise the value of the die."""
        self._value = randint(1, 6)
