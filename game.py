#imports
from guizero import App, Box, PushButton, Text, Window

#Functions
def clear_board():
    """ Resets the game board for a new game. """
    for row in board_squares:
        for button in row:
            button.text = " "
            button.enable()
    global turn
    turn = "X"
    message.value = "It is your turn, " + turn


def choose_square(x, y):
    board_squares[x][y].disable()

    board_squares[x][y].text = turn
    board_squares[x][y].text_size = 44
    if turn == "X":
        board_squares[x][y].text_color = "red"
    else:
        board_squares[x][y].text_color = "yellow"

    check_win()
    toggle_player()

def toggle_player():
    """ Switches the current player from X to O or vice versa. """
    global turn
    if turn == "X":
        turn = "O"
        message.text_color = "red"
    else:
        turn = "X"
        message.text_color = "yellow"
    # Only update the turn message if the game is still ongoing
    if not winner and moves_taken() < 9:
        message.value = "It is your turn, " + turn


def check_win():
    """ Checks all win conditions (horizontal, vertical, diagonal) and for a draw. """
    global winner
    winner = None

    # Check rows for a winner
    for row in range(3):
        if (board_squares[row][0].text == board_squares[row][1].text == board_squares[row][2].text) and board_squares[row][0].text != " ":
            winner = board_squares[row][0].text
            break # Exit loop once a winner is found

    # Check columns for a winner if one hasn't been found yet
    if not winner:
        for col in range(3):
            if (board_squares[0][col].text == board_squares[1][col].text == board_squares[2][col].text) and board_squares[0][col].text != " ":
                winner = board_squares[0][col].text
                break

    # Check diagonals for a winner if one hasn't been found yet
    if not winner:
        if (board_squares[0][0].text == board_squares[1][1].text == board_squares[2][2].text) and board_squares[0][0].text != " ":
            winner = board_squares[0][0].text
        elif (board_squares[0][2].text == board_squares[1][1].text == board_squares[2][0].text) and board_squares[0][2].text != " ":
            winner = board_squares[0][2].text

    if winner:
        message.value = winner + " wins!"
        disable_all_buttons()
    elif moves_taken() == 9:
        message.value = "It's a draw!"
        message.text_color = "cyan"

def moves_taken():
    """ Counts the number of moves taken so far. """
    moves = 0
    for row in board_squares:
        for col in row:
            if col.text in ["X", "O"]:
                moves += 1
    return moves

def disable_all_buttons():
    """ Disables all buttons on the board once the game is over. """
    for row in board_squares:
        for button in row:
            button.disable()

#--- App Setup ---

#Variables
turn = "X"
winner = None

#App
app = App("Tic Tac Toe", width = 500, height = 500, bg = 'black')

# Message display
message = Text(app, text="It is your turn, " + turn + "!", font = "Times New Roman", size = 20, color = "white")
Box(app, height=20, width="fill") 
# Game board
board = Box(app, layout="grid", border = True)
board.set_border(2,"red")

for i in range(3):
    board.tk.grid_columnconfigure(i, weight=4)
    board.tk.grid_rowconfigure(i, weight=2)

board_squares = [[None, None, None], [None, None, None], [None, None, None]]

for x in range(3):
    for y in range(3):
        button = PushButton(
            board,
            text=" ",
            grid=[x, y],
            height=1,
            width=1,
            # Link the choose_square function to the button, passing its coordinates
            command=choose_square,
            args=[x, y]
        )
        button.text_size = 45
        button.tk.grid(sticky="nsew")
        board_squares[x][y] = button
Box(app, height=5, width="fill") 

# Reset button
reset_button = PushButton(app, text="New Game", command=clear_board)

app.display()