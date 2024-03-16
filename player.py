from die import Die


class Player:

    def __init__(self, die=Die(), is_cpu=False):
        self._die = die
        self.is_cpu = is_cpu
        self._counter = 10

    @property
    def die(self):
        return self._die

    def roll_die(self):
        pass

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1
