class Round:

    def __init__(self, number, display):
        self.number = number
        self.display = display

    def play_round(self):
        self.display(
            f'Round {self.number}:\n'
            '--------\n'
        )  # fmt: skip
