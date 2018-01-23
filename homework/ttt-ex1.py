def solicit_move (player):
    #player is either "X" or "Y"
    move = input("{}'s move >: ".format(player))
    return move

def valid_move (move):
    #move is the string, valid_move should be evoked within the game body using the return from solicit_move as the move
    if move == "quit":
        pass
    elif move not in mark_positions.keys():
        print("Sorry, that is not a valid move. Please try again.")
        return False
    elif mark_positions[move] != " ":
        print("Sorry, {} is already in that position. Please try again.".format(mark_positions[move]))
        return False
    else:
        return True

def update_positions (move_valid):
    #move_valid is a Boolean, should be determined by the valid_move function
    while move_valid == False:
        move = solicit_move(player)
        move_valid = valid_move(move)
    if move_valid == True:
        mark_positions[move] = player

def draw_board (mark_positions):
    if move == "quit":
        pass
    else:
        board_string = "CURRENT BOARD:\n {} | {} | {} \n-----------\n {} | {} | {} \n-----------\n {} | {} | {}".format(*mark_positions.values())
        print(board_string)

def change_player (player):
    if player = "X":
        return "Y"
    else:
        return "X"

def game_over_status (mark_positions):
    if move == "quit":
        return True
    elif mark_positions.values[0]==mark_positions.values[1]==mark_positions.values[2] or mark_positions.values[3]==mark_positions.values[4]==mark_positions.values[5] or mark_positions.values[6]==mark_positions.values[7]==mark_positions.values[8]:
        print("Player {} wins!".format(player))
        return True
    elif mark_positions.values[0]==mark_positions.values[3]==mark_positions.values[6] or mark_positions.values[1]==mark_positions.values[4]==mark_positions.values[7] or mark_positions.values[2]==mark_positions.values[5]==mark_positions.values[8]:
        print("Player {} wins!".format(player))
        return True
    elif mark_positions.values[0]==mark_positions.values[4]==mark_positions.values[8] or mark_positions.values[2]==mark_positions.values[4]==mark_positions.values[6]:
        print("Player {} wins!".format(player))
        return True
    elif " " not in mark_positions.values():
        print("It's a draw!")
        return True
    else:
        return False

def ttt (player = "X"):
    mark_positions={"NW":" ", "N":" ", "NE":" ","W":" ", "C":" ", "E":" ", "SW": " ", "S": " ", "SE": " "}
    game_over_status=False
    pass
    #this function takes the parameter of the current player, ad will assume that "X" is starting unless told otherwise
    #this function invokes all the other functions defined above to allow the user to play the tictactoe game
#make actual working code of the ttt game
