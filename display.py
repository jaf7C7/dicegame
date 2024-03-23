class Display:

    def __init__(self, display):
        self.display = display

    def game_welcome(self):
        self.display(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )
