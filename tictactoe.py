import turtle

screen = turtle.Screen()
screen.title("Tic Tac Toe")
screen.setup(width=600, height=600)

drawer = turtle.Turtle()
drawer.speed(0)
drawer.hideturtle()
drawer.penup()

turn_display = turtle.Turtle()
turn_display.hideturtle()
turn_display.penup()
turn_display.goto(0, 260)
turn_display.write("X to move", align="center", font=("Arial", 24, "normal"))

board = [["" for _ in range(3)] for _ in range(3)]
turn = "X"
game_over = False

def draw_grid():
    for i in [-100, 100]:
        drawer.goto(-300, i)
        drawer.pendown()
        drawer.goto(300, i)
        drawer.penup()
        drawer.goto(i, -300)
        drawer.pendown()
        drawer.goto(i, 300)
        drawer.penup()

def get_cell(x, y):
    row = 2 - (y + 300) // 200
    col = (x + 300) // 200
    return int(row), int(col)

def draw_symbol(row, col, symbol):
    x_center = col * 200 - 300 + 100
    y_center = 300 - row * 200 - 100
    drawer.goto(x_center, y_center)
    drawer.write(symbol, align="center", font=("Arial", 48, "normal"))

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    if all(board[i][j] != "" for i in range(3) for j in range(3)):
        return "Tie"
    return None

def handle_click(x, y):
    global turn, game_over
    if game_over:
        return
    row, col = get_cell(x, y)
    if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != "":
        return
    board[row][col] = turn
    draw_symbol(row, col, turn)
    winner = check_winner()
    if winner:
        turn_display.clear()
        if winner == "Tie":
            turn_display.write("It's a tie!", align="center", font=("Arial", 24, "normal"))
        else:
            turn_display.write(f"{winner} wins!", align="center", font=("Arial", 24, "normal"))
        game_over = True
        return
    turn = "O" if turn == "X" else "X"
    turn_display.clear()
    turn_display.write(f"{turn} to move", align="center", font=("Arial", 24, "normal"))

draw_grid()
screen.onclick(handle_click)
screen.mainloop()

