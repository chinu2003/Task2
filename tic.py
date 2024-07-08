import tkinter as tk
from tkinter import messagebox

# Initialize global variables
current_player = "X"
board = [""] * 9

# Function to check for a win or tie
def check_winner():
    global board
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]  # diagonal
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]
    if "" not in board:
        return "Tie"
    return None

# Function to handle button click
def button_click(btn, idx):
    global current_player, board
    if board[idx] == "" and btn["text"] == "":
        btn["text"] = current_player
        board[idx] = current_player
        winner = check_winner()
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn["text"] = ""

# Main program starts here
if __name__ == "__main__":
    # Setting up the main window
    window = tk.Tk()
    window.title("Tic-Tac-Toe")

    # Create buttons for the Tic-Tac-Toe grid
    buttons = []
    for i in range(9):
        btn = tk.Button(window, text="", font=("Arial", 24), width=5, height=2, command=lambda i=i: button_click(buttons[i], i))
        btn.grid(row=i//3, column=i%3)
        buttons.append(btn)

    # Add reset button
    reset_btn = tk.Button(window, text="Reset", font=("Arial", 14), command=reset_game)
    reset_btn.grid(row=3, column=0, columnspan=3)

    window.mainloop()
