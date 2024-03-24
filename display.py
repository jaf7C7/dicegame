class Display:

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

    def display_game_results(self, winner):
        self.display('And the winner is...\n' f'{winner}!\n' '\n')

    def display_round_welcome(self, round_number):
        self.display(f'Round {round_number}:\n' '--------\n')

    def display_player_die_values(self, p1_die, p2_die):
        self.display(
            '\n' f'Player 1 rolled: {p1_die}\n' f'Player 2 rolled: {p2_die}\n'
        )

    def display_round_result(self, winner, is_tie):
        msg = "It's a Tie!" if is_tie else f'WINNER: {winner}'
        self.display(
            '*************************\n'
            f'Round 1: {msg}\n'
            '*************************\n'
            '\n'
        )

    def display_player_counters(self, p1_counter, p2_counter):
        self.display(
            '~~~~ Player counters: ~~~~\n'
            f'Player 1: {p1_counter}\n'
            f'Player 2: {p2_counter}\n'
            '\n'
        )

    def prompt_player_roll(self, player):
        self.display('Player 1: Press any key to roll your die... ')
