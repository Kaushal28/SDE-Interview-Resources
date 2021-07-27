import random

from src.models.player import Player
from src.services.game_service import GameService
from src.models.ladder import Ladder
from src.models.snake import Snake


def driver():
    game_service = GameService()

    players = []
    for idx in range(2):
        players.append(Player(name=f"abc_{idx}", id=str(idx)))

    game_service.players = players

    # add random snakes and ladders
    game_service.set_ladders(
        [Ladder(random.randint(1, 50), random.randint(51, 100)) for _ in range(8)]
    )
    game_service.set_snakes(
        [Snake(random.randint(51, 100), random.randint(1, 50)) for _ in range(8)]
    )

    # start the game
    game_service.start_game()


driver()
