class Game:
    def __init__(self, display):
        self.display = display

    def play(self):
        self.display(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )

    def play_round(self):
        self.display(
            'Round 1:\n'
            '--------\n'
        )  # fmt: skip
