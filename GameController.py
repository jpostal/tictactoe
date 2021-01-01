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

    __players = ["X", "0"]
    __first = ""
    __current_turn = {}
    __game_matrix = []
    __game_over = False

    def __init__(self, matrix_size=3):
        self.__create_matrix(matrix_size)
        self.__set_players_order()

    def __create_matrix(self, dimension):
        self.__game_matrix = [['_' for _ in range(dimension)] for _ in range(dimension)]

    def __set_players_order(self):
        player_scores = {}

        for player in self.__players:
            input("Player %s press enter to roll dice." % (player))
            player_scores[player] = random.randint(1, 10)
            print(player_scores[player])

        self.__first = max(player_scores, key=lambda key: player_scores[key]) # getting biggest score
        print("Player %s starts" % str(self.__first))

    def get_player_turn(self):
        if not self.__current_turn: # null test, means new game
            self.__current_turn = self.__first

        elif self.__current_turn == self.__players[0]:
            self.__current_turn = self.__players[1]

        elif self.__current_turn == self.__players[1]:
            self.__current_turn = self.__players[0]

        return self.__current_turn

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
        