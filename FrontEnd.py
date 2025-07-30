import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from BackEnd import *

def menu(player_turn, board):
    #Menu Settings
    window = tk.Tk()
    window.title("Tic Tac Toe")
    
    #Title
    title = ttk.Label(window, text=f"Player {player_turn}'s turn")
    title.grid(row=0, column=0, columnspan=3, pady=10)  # Sets grid
    
    #Buttons which calls to button_click
    buttons = []
    for i in range(9):
        button = ttk.Button(
            window, 
            text=board[i], 
            width=10,
            command=lambda pick=i: button_click(pick, buttons, title)
        )

        #Sets grid positions
        row_pos = (i // 3) + 1  
        col_pos = i % 3
        button.grid(row=row_pos, column=col_pos, padx=5, pady=5)
        buttons.append(button)
    
    window.mainloop()


def button_click(pick, buttons, title):
    #Convert pick to 1-indexed for frontend
    frontend_pick = pick + 1

    #Validate input
    if game.board[pick] == "X" or game.board[pick] == "O":
        tk.messagebox.showinfo(title="Invalid Move", message="Square already taken, please choose another.")

    else:
        #Makes the move, updates the board and check for win
        make_move(str(frontend_pick), game.board, game.player_turn)
        result = win_check(game.board, game.player_turn)
        update_board(pick, buttons, game.player_turn, title)

        #If there is a win or draw, show the result and exit
        if result is not None:
            tk.messagebox.showinfo(title=result, message=f"Game Over, {result}")
            exit()

    
def update_board(pick, buttons, player_turn, title):
    #Updates the player turn
    game.player_turn = turn(game.board, game.player_turn)
    
    #Updates the menu information
    title.config(text=f"Player {game.player_turn}'s turn")
    buttons[pick].config(text=player_turn)

game = TTT()  

menu(game.player_turn,game.board)