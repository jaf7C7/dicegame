from die import Die


class Player:

    def __init__(self, die=Die()):
        self.die = die
        self.is_cpu = None
