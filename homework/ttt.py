def solicit_move (player):
    pass
    #this function takes the parameter of the player turn (X or O)
    #the funciton asks the user for the input, with a formatted string letting the user know whose turn it is
    #the function returns whatever the user inputs as their move

def valid_move (move, mark_positions):
    pass
    #this function takes the player move as a string and the current positions dictionary and determines that the move is a key in that dictionary and that the dictionary does not aready have X or O as a values
    #this function returns a Boolean value of True when the move is valid and False when the move is not valid

def draw_board (mark_positions):
    pass
    #this function takes the parameter of the current board layout dictionary
    #this function transforms that dictionary into a formatted string with all the marks in the right place and prints that string
    #this function is just to draw the board and returns the special value None

def winner (mark_positions):
    pass
    #this function takes the paramter of the board layout dictionary
    #this function uses if, else statements to determine if the board matches any of the winning combinations, and if so, it returns the winner based on who the currenet player is
    #this function returns the winner, which can be "X", "O", or "None" if a winning combination is not found

def game_over_status (winner):
    pass
    #this function takes the input of the winner, which can be X, O or None
    #if the winner is None, the 

def change_player (player):
    pass
    #this function takes the single parameter of player
    #the function always changes the player, since there are only two players and returns the updated player
