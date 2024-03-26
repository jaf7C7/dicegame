class UI:

    def __init__(self, display):
        self.display = display

    def display_game_welcome(self):
        self.display(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )

    def display_game_over(self):
        self.display(
            '===================\n'
            '**** GAME OVER ****\n'
            '===================\n'
            '\n'
        )

    def display_winner(self, winner):
        self.display('And the winner is...\n' f'{winner}!\n' '\n')

    def display_round_welcome(self, round_number):
        self.display(f'Round {round_number}:\n' '--------\n')

    def display_player_die_values(self, players):
        self.display('\n')
        for player in players:
            self.display(f'{player} rolled: {player.die.value}\n')

    def display_round_result(self, winner):
        result = f'WINNER: {winner}' if winner is not None else "It's a Tie!"
        self.display(
            '*************************\n'
            f'Round 1: {result}\n'
            '*************************\n'
            '\n'
        )

    def display_player_counters(self, players):
        self.display('~~~~ Player counters: ~~~~\n')
        for player in players:
            self.display(f'{player}: {player.counter}\n')

    def get_user_input(self, player):
        self.display(f'{player}: Press any key to roll your die... ')
