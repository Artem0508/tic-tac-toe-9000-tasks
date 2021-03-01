from abc import ABC, abstractmethod
from typing import List, Callable
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class TicTacToeTurn:
    player_id: str
    x_coordinate: int
    y_coordinate: int


@dataclass
class TicTacToeGameInfo:
    game_id: str
    field: List[List[str]]
    sequence_of_turns: List[TicTacToeTurn]
    first_player_id: str
    second_player_id: str
    winner_id: str # а какие могут быть варианты?


class AbstractTicTacToeGame(ABC):
    @abstractmethod
    def __init__(
            self,
            game_id: str,
            first_player_id: str,
            second_player_id: str,
            strategy: Callable[[TicTacToeGameInfo], TicTacToeTurn] = None
        ) -> None:
        """пока просто раскладываем по полям"""
        self.__game_id = game_id
        self.__first_player_id = first_player_id
        self.__second_player_id = second_player_id
        self.__winner_id = ""
        self.__strategy = strategy
        self.__turns: List[TicTacToeTurn] = []

    @abstractmethod
    def get_game_info(self) -> TicTacToeGameInfo:
        result = TicTacToeGameInfo(
            game_id=self.__game_id,
            field=[
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ],
            sequence_of_turns=deepcopy(self.__turns),
            first_player_id=self.__first_player_id,
            second_player_id=self.__second_player_id,
            winner_id=self.__winner_id
        )
        for turn in self.__turns:
            if turn.player_id == self.__first_player_id:
                ch = "X"
            else:
                ch = "O"
            result.field[turn.x_coordinate][turn.y_coordinate] = ch
        return result