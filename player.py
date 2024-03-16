from die import Die


class Player:

    def __init__(self, die=Die(), is_cpu=False):
        self.die = die
        self.is_cpu = is_cpu
        self.counter = 10
