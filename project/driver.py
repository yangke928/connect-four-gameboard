'''Ke Yang
   cs5001
   Project
   April 1st
'''

import game

def input_size():
    '''
    Function: input_size
    Parameters: none
    Return: the number of columns and rows that the player input
    Do : check the columns and rows the play input is valid and reasonable
    '''
    is_invalid = True
    while is_invalid:
        num_columns = input("How many colunms do you want in the board?")
        num_rows = input("How many rows do you want in the board?")
        if num_columns.isdigit() and num_columns.isdigit():
            if 1 < int(num_columns) < 10 and 1 < int(num_rows) < 10:
                is_invalid = False
        if is_invalid:
            print("Please input reasonable size '<10' !")
    return int(num_columns), int(num_rows)


def main():
    print("Man vs Man  or  Man vs Computer ?")
    choice = 0
    while choice not in {1, 2}:
        choice = input("Man vs Man: type 1, Man vs Computer: type 2.\n")
        choice = int(choice) if choice.isdigit() else 0

    num_columns, num_rows = input_size()
    my_game = game.Game("red_score.txt", "yellow_score.txt", num_columns, num_rows)
    my_game.init_chessboard()
    if choice == 1:
        my_game.launcher_manvsman()
    else:
        my_game.launcher_manvscomputer()

main()
