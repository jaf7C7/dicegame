from random import randint

class Die():

    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    def roll(self):
        self._value = randint(1, 7)
