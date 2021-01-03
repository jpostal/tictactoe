from GameController import GameController as gc
from BColors import BColors as bc


class MainController(object):
    """
    Application Entrypoint.
    """
    __gc = gc()
    __current_player = ""

    def __request_player_position_input(self):

        # TODO: Input test to admit only numbers.
        move = input("Player %s select line and column separated by whitespace to assign\n" %
                     self.__current_player).split(" ")

        if len(move) > 2:
            print(f"{bc.WARNING}Don´t be silly, it's just 2 inputs.{bc.ENDC}")

        line_pos, col_pos = move[:2]
        success = self.__send_player_input(int(line_pos), int(col_pos))

        if not success:
            self.__request_player_position_input()

    def __send_player_input(self, line, col):
        if line > len(self.__gc.get_matrix()):
            print("Invalid position for line")
            return False
        elif col > len(self.__gc.get_matrix()):
            print("Invalid position for column")
            return False
        else:
            self.__gc.assign_player_move(self.__current_player, line, col)
            return True

    def main(self):
        # TODO: Loop to control turns and end game.

        # self.__current_player = self.__gc.get_player_turn()
        # print("its %s turn now" % str(self.__current_player))
        #
        # self.__request_player_position_input()
        # self.__gc.print_matrix()
        self.__gc.set_hcoded_player_move()
        self.__gc.print_matrix()
        self.__gc.game_over_test()


if __name__ == '__main__':
    m = MainController()
    m.main()
