from GameController import GameController as gc

if __name__ == '__main__':

    game_controller = gc()

    # while game_controller.

    current_player = game_controller.get_player_turn()
    print("its %s turn now" % str(current_player))

    game_controller.assign_player_move(current_player,1,1)
    game_controller.print_matrix()


