class Round:

    def __init__(self, display):
        self.display = display

    def play_round(self):
        self.display(
            'Round 1:\n'
            '--------\n'
        )  # fmt: skip
