from die import Die


class Player:
    """A human or computer player."""

    def __init__(self, die=None, is_cpu=False, number=None):
        if die is None:
            die = Die()
        self._die = die
        self.is_cpu = is_cpu
        self._counter = 5
        self.number = number

    def __str__(self):
        return f'Player {self.number}'

    @property
    def die(self):
        return self._die

    def roll_die(self):
        """Roll the player's die."""
        self._die.roll()

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        """Increment the player's counter by 1."""
        self._counter += 1

    def decrement_counter(self):
        """Decrement the player's counter by 1."""
        self._counter -= 1
