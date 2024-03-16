from die import Die


class Player:

    def __init__(self, die=Die(), is_cpu=False):
        self._die = die
        self.is_cpu = is_cpu
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        pass
