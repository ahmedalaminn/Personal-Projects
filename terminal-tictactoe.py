board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
turn = "X"
xCord = None
yCord = None
wrongNumber = True
turnCounter = 0
tie = False


def print_board():
    print("  0 " + "1 " + "2 ")
    print("0 " + board[0] + " " + board[1] + " " + board[2])
    print("1 " + board[3] + " " + board[4] + " " + board[5])
    print("2 " + board[6] + " " + board[7] + " " + board[8])
print_board()

def did_they_win():
    if board[0] == board[1] == board[2] != "-":
        return True
    elif board[3] == board[4] == board[5] != "-":
        return True
    elif board[6] == board[7] == board[8] != "-":
        return True
    elif board[0] == board[4] == board[8] != "-":
        return True
    elif board[2] == board[4] == board[6] != "-":
        return True
    elif board[0] == board[1] == board[2] != "-":
        return True
    elif board[0] == board[3] == board[6] != "-":
        return True
    elif board[1] == board[4] == board[7] != "-":
        return True
    elif board[2] == board[5] == board[8] != "-":
        return True
    else:
        return False

def finding_spot(xCord, yCord):
    if xCord == 0 and yCord == 0:
        return str(board[0])
    elif xCord == 1 and yCord == 0:
        return str(board[1])
    elif xCord == 2 and yCord == 0:
        return str(board[2])
    elif xCord == 0 and yCord == 1:
        return str(board[3])
    elif xCord == 1 and yCord == 1:
        return str(board[4])
    elif xCord == 2 and yCord == 1:
        return str(board[5])
    elif xCord == 0 and yCord == 2:
        return str(board[6])
    elif xCord == 1 and yCord == 2:
        return str(board[7])
    elif xCord == 2 and yCord == 2:
        return str(board[8])

def picking_spot(xCord, yCord, turn):
    if xCord == 0 and yCord == 0:
        board[0] = turn
    elif xCord == 1 and yCord == 0:
        board[1] = turn
    elif xCord == 2 and yCord == 0:
        board[2] = turn
    elif xCord == 0 and yCord == 1:
        board[3] = turn
    elif xCord == 1 and yCord == 1:
        board[4] = turn
    elif xCord == 2 and yCord == 1:
        board[5] = turn
    elif xCord == 0 and yCord == 2:
        board[6] = turn
    elif xCord == 1 and yCord == 2:
        board[7] = turn
    elif xCord == 2 and yCord == 2:
        board[8] = turn


while not did_they_win():
    if turn == "X":
        while True:
            try:
                xCord = int(input("It's X's turn! Pick the column for the coordinate you want to put your X: "))
                yCord = int(input("Still X's turn! Now enter the row for that coordinate!"))

            except ValueError:
                print("Invalid input. No spaces, please enter a number between 0-2.")
                continue
            else:
                if xCord > 2 or yCord > 2:
                    wrongNumber = True
                    print("Coordinates entered are not on grid. Please pick a column/row number on the coordinate "
                          "grid, between 0-2.")
                elif not finding_spot(xCord, yCord) == "-":
                    wrongNumber = True
                    print("Spot has already been taken. Please enter another set of coordinates.")
                else:
                    break

        picking_spot(xCord, yCord, "X")
        print_board()
        turnCounter += 1
        if did_they_win():
            break
        if turnCounter == 9:
            tie = True
            break
        turn = "O"
    else:
        while True:
            try:
                xCord = int(input("It's O's turn! Pick the column for the coordinate you want to put your O: "))
                yCord = int(input("Still O's turn! Now enter the row for that coordinate!"))

            except ValueError:
                print("Invalid input. No spaces, please enter a number between 0-2.")
                continue
            else:
                if xCord > 2 or yCord > 2:
                    wrongNumber = True
                    print("Coordinates entered are not on grid. Please pick a column/row number on the coordinate "
                          "grid, between 0-2.")
                elif not finding_spot(xCord, yCord) == "-":
                    wrongNumber = True
                    print("Spot has already been taken. Please enter another set of coordinates.")
                else:
                    break

        picking_spot(xCord, yCord, "O")
        print_board()
        turnCounter += 1
        if did_they_win():
            break
        if turnCounter == 9:
            tie = True
            break
        turn = "X"

if not tie:
    print("Congratulations! " + turn + " won!")
else:
    print("No winner :( Tie")
