from typing import List

from src.models.board import Board
from src.models.player import Player
from src.models.snake import Snake
from src.models.ladder import Ladder
from src.services.dice_service import DiceService


class GameService:
    def __init__(self, board_size: int = 100, num_dice: int = 1):
        self.board_size = board_size
        self.num_dice: int = num_dice
        self.board = Board(board_size)
        self._players: List[Player] = []
        self.total_players = 0

    @property
    def players(self) -> List[Player]:
        return self._players

    @players.setter
    def players(self, players: List[Player]):
        self.total_players = len(players)
        self._players = players

    def set_snakes(self, snakes: List[Snake]):
        """
        Set given snakes in current game.
        """
        self.board.snakes = snakes

    def set_ladders(self, ladders: List[Ladder]):
        """
        Set given ladders in current game.
        """
        self.board.ladders = ladders

    def is_completed(self, cont_till_last_player: bool = False) -> bool:
        """Check whether the game is completed or not."""
        if cont_till_last_player:
            return len(self.players) == 1

        return len(self.players) < self.total_players

    def roll_dice(self) -> int:
        """Roll one or more dice one or multiple times."""
        steps = 0
        for num in range(self.num_dice):
            steps += DiceService.roll()

        return steps

    def has_player_won(self, player: Player) -> bool:
        """Check whether the given player has won the game."""
        player_piece_position = self.board.player_pieces.get(player.id)
        return player_piece_position == self.board_size

    def get_new_position(self, player: Player, steps: int) -> int:
        """Move the given player's piece by given steps."""
        player_piece_position = self.board.player_pieces.get(player.id, 0)

        if player_piece_position + steps > self.board_size:
            return player_piece_position
        else:
            new_position = player_piece_position + steps
            while True:
                is_snake = False
                for snake in self.board.snakes:
                    if snake.start == new_position:
                        new_position = snake.end
                        print(
                            f"{player.name} swallowed by snake from {snake.start} to {snake.end}."
                        )
                        is_snake = True

                is_ladder = False
                for ladder in self.board.ladders:
                    if ladder.start == new_position:
                        new_position = ladder.end
                        print(
                            f"{player.name} climbed a ladder from {ladder.start} to {ladder.end}."
                        )
                        is_ladder = True

                if not is_ladder and not is_snake:
                    break

            return new_position

    def start_game(self):
        """
        Start the Snake and Ladder game.
        """
        while not self.is_completed():
            # roll the dice
            steps = self.roll_dice()
            # get the player having turn
            player = self.players.pop(0)
            # move his/her piece
            new_position = self.get_new_position(player, steps)
            self.board.player_pieces[player.id] = new_position
            print(f"{player.name} rolled {steps} and moved to {new_position}.")
            if self.has_player_won(player):
                print(f"{player.name} won the game!")
                self.board.player_pieces.pop(player.id)
            else:
                self.players.append(player)
