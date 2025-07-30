class TTT:
    def __init__(self):
        self.board = ["-"] * 9
        self.valid_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.player_turn = "X"


def make_move(pick, board, player_turn):
    #Sets the board position to the X or O
    board[int(pick) - 1] = player_turn


def win_check(board, player_turn):
    #Checks for winning conditions
    #Checks for row
    for i in range(0, 9, 3):
        if board[i] == player_turn and board[i+1] == player_turn and board[i+2] == player_turn:
            return f"{player_turn} wins!"
    
    #Checks for collumn
    for i in range(0,3):
        if board[i] == player_turn and board[i+3] == player_turn and board[i+6] == player_turn:
            return f"{player_turn} wins!"
        
    #Checks for diagonal
    if (board[0] == player_turn and board[4] == player_turn and board[8] == player_turn) or \
       (board[2] == player_turn and board[4] == player_turn and board[6] == player_turn):
            return f"{player_turn} wins!"
    
    #Checks for draw
    if board.count("-") == 0:
        return "It's a draw!"

#Decides whose turn it is
def turn(board, player_turn):
    if player_turn == "X":
        player_turn = "O"
        return player_turn
    else:
        player_turn = "X"
        return player_turn
    