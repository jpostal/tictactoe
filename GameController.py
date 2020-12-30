import numpy as np
import warnings
import random


class GameControllerMeta(type):
    """
    Singleton for Game Controller
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            warnings.warn("You already have an instance of GameController running, use it!!")

        return cls._instances[cls]


class GameController(metaclass=GameControllerMeta):

    __players = {"player_1": "X", "player_2": "0"}
    __first = {}
    __game_matrix = []
    __game_over = False

    def __init__(self, matrix_size=3):
        self.__create_matrix(matrix_size)
        self.__set_players_order()

    def __create_matrix(self, dimension):
        self.__game_matrix = [['_' for _ in range(dimension)] for _ in range(dimension)]

    def __set_players_order(self):
        player_scores = []

        for i in range(len(self.__players)):
            input("Player %s press enter to roll dice." % (i + 1))
            player_scores.append(random.randint(0, 10))
            print(player_scores[i])

        # TODO: Lazy solution...
        if player_scores[0] > player_scores[1]:
            self.__first = self.__players['player_1']
            print("Player 1 Starts")
        else:
            self.__first = self.__players['player_2']
            print("Player 2 Starts")

    def get_matrix(self):
        return self.__game_matrix

    def assign_player_move(self, player, line_pos, col_pos):
        self.__game_matrix[line_pos][col_pos] = player

    def print_matrix(self):
        print(np.array(self.__game_matrix))

    def is_game_over(self):
        return self.__game_over

    def set_game_over(self):
        self.__game_over = True
        