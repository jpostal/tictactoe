import numpy as np
import warnings
import random
from BColors import BColors as bc


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
    __dimension = 0
    __players = {"X": 2, "O": 1}
    __first = ""
    __current_turn = {}
    __game_matrix = []
    __game_over = False

    def __init__(self, matrix_size=3):
        self.__create_matrix(matrix_size)
        # self.__set_players_order()

    def __create_matrix(self, dimension):
        self.__game_matrix = np.zeros(shape=(dimension, dimension), dtype=int)
        self.__dimension = dimension

    def __set_players_order(self):
        player_scores = {}

        for player in self.__players:
            input("Player %s press enter to roll dice." % (player))
            player_scores[player] = random.randint(1, 10)
            print(player_scores[player])

        self.__first = max(player_scores, key=lambda key: player_scores[key])  # getting biggest score
        print("Player %s starts" % str(self.__first))

    def get_player_turn(self):

        # TODO: Could this be better?
        if not self.__current_turn:  # null test, means new game
            self.__current_turn = self.__first

        elif self.__current_turn == self.__players['X']:
            self.__current_turn = self.__players['O']

        elif self.__current_turn == self.__players['O']:
            self.__current_turn = self.__players['X']

        return self.__current_turn

    def get_matrix(self):
        return self.__game_matrix

    def assign_player_move(self, player, line_pos, col_pos):
        self.__game_matrix[col_pos][line_pos] = self.__players[player]

    def print_matrix(self):
        print(f"%s" % np.array2string(self.__game_matrix).replace("1", "O").replace("2", "X").replace("0", "_"))

    def is_game_over(self):
        return self.__game_over

    def set_game_over(self):
        self.__game_over = True

    def game_over_test(self):
        winner = []

        # TODO: Improve these conditions and test diagonal matches
        for i in range(self.__dimension):
            line = np.array(self.__game_matrix[i, :])
            column = np.array(self.__game_matrix[:, i])
            if column.all(axis=0):
                winner = [x for x in self.__players.keys() if self.__players[x] == column[0]]
                print(f"{bc.OKBLUE}%s{bc.ENDC}" % column.reshape(self.__dimension, 1))

            elif line.all(axis=0):
                winner = [x for x in self.__players.keys() if self.__players[x] == line[0]]
                print(f"{bc.OKBLUE}%s{bc.ENDC}" % line.reshape(1, self.__dimension))
        if winner:
            print("Player %s Won!" % winner)

    def set_hcoded_player_move(self):
        self.assign_player_move('X', 0, 0)
        self.assign_player_move('X', 1, 0)
        self.assign_player_move('X', 2, 0)
