from typing import List, Dict
from collections import defaultdict

from .ladder import Ladder
from .snake import Snake


class Board:
    """Snake and Ladder board object."""

    def __init__(self, size: int):
        self.size = size
        self.snakes: List[Snake] = []
        self.ladders: List[Ladder] = []
        self.player_pieces: Dict[str, int] = defaultdict(int)
