from player import Player


class Game:
    """A game to be played by two players over a number of rounds"""

    def __init__(
        self, player_1=Player(), player_2=Player(is_cpu=True), display=print
    ):
        self.player_1 = player_1
        self.player_2 = player_2
        self.display = display
        self.round_number = 0
        self.game_winner = None

    def play(self):
        self._display_game_welcome()

        while not self.game_over():
            self.play_round()

        self._display_game_over()

    def play_round(self):
        self.round_number += 1
        self._display_round_welcome()

        for player in (self.player_1, self.player_2):
            if not player.is_cpu:
                input('Press any key to roll your die... ')
            player.roll_die()

        self._display_die_values()
        self._get_round_winner()
        self._display_player_counters()

    def game_over(self):
        if self.player_1.counter == 0:
            self.game_winner = 'Player 1'
        elif self.player_2.counter == 0:
            self.game_winner = 'Player 2'

        return self.game_winner is not None

    def _display_game_welcome(self):
        self.display(
            '=========================\n'
            'Welcome To The Dice Game!\n'
            '=========================\n'
        )

    def _display_game_over(self):
        self.display(
            '===================\n'
            '**** GAME OVER ****\n'
            '===================\n'
            '\n'
            'And the winner is...\n'
            f'{self.game_winner}!\n'
            '\n'
        )

    def _display_round_welcome(self):
        self.display(
            f'Round {self.round_number}:\n'
            '--------\n'
        )  # fmt: skip

    def _display_die_values(self):
        self.display(
            '\n'
            f'Player 1 rolled: {self.player_1.die.value}\n'
            f'Player 2 rolled: {self.player_2.die.value}\n'
        )

    def _get_round_winner(self):
        if self.player_1.die.value == self.player_2.die.value:
            self.round_result = "It's a Tie!"
        elif self.player_1.die.value > self.player_2.die.value:
            self.round_result = 'WINNER: Player 1'
            self.player_1.decrement_counter()
            self.player_2.increment_counter()
        else:
            self.round_result = 'WINNER: Player 2'
            self.player_2.decrement_counter()
            self.player_1.increment_counter()

    def _display_player_counters(self):
        self.display(
            '*************************\n'
            f'Round {self.round_number}: {self.round_result}\n'
            '*************************\n'
            '\n'
            '~~~~ Player counters: ~~~~\n'
            f'Player 1: {self.player_1.counter}\n'
            f'Player 2: {self.player_2.counter}\n'
            '\n'
        )
