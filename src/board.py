def print_instructions_to_console():
    print("The following is a Tic Tac Toe board.\nPlease select a location where you \nwant to place your symbols!")
    for row in range(3):
        for col in range(3):
            if col < 2:
                print(f" {3 * row + col + 1}  |", end="")
            else:
                print(f" {3 * row + col + 1}  ", end="")
        if row < 2:
            print("\n______________\n")


class gameBoard:
    def __init__(self):
        self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.X = 1
        self.O = 2

    def __str__(self):
        repr_str = ""
        for row in range(3):
            for col in range(3):
                if col < 2:
                    if self.state[row][col] == 0:
                        repr_str += "   |"
                    elif self.state[row][col] == self.X:
                        repr_str += " X |"
                    else:
                        repr_str += " O |"
                else:
                    if self.state[row][col] == 0:
                        repr_str += "   "
                    elif self.state[row][col] == self.X:
                        repr_str += " X "
                    else:
                        repr_str += " O "
            if row < 2:
                repr_str += "\n____________\n"
        return repr_str

    def isEmpty(self, row, col):
        return self.state[row][col] == 0

    def update(self, row, col, player):
        if player + 1 == self.X:
            self.state[row][col] = self.X
        else:
            self.state[row][col] = self.O

    def isWin(self):
        # check rows
        for r in range(3):
            if self.state[r][0] == self.state[r][1] and self.state[r][1] == self.state[r][2] and self.state[r][0] != 0:
                if self.state[r][0] == 1:
                    print("Congrats! Player 1 Wins!")
                if self.state[r][0] == 2:
                    print("Congrats! Player 2 Wins!")
                return True

        # check columns
        for col in range(3):
            col_collector = []
            for row in range(3):
                col_collector.append(self.state[row][col])
            if col_collector[0] == col_collector[1] and col_collector[1] == col_collector[2] and col_collector[0] != 0:
                if self.state[0][col] == 1:
                    print("Congrats! Player 1 Wins!")
                if self.state[0][col] == 2:
                    print("Congrats! Player 2 Wins!")
                return True

        # main diagonal
        if self.state[0][0] == self.state[1][1] and self.state[1][1] == self.state[2][2] and self.state[1][1] != 0:
            if self.state[0][0] == 1:
                print("Congrats! Player 1 Wins!")
            if self.state[0][0] == 2:
                print("Congrats! Player 2 Wins!")
            return True

        # secondary diagonal
        if self.state[0][2] == self.state[1][1] and self.state[1][1] == self.state[2][0] and self.state[1][1] != 0:
            if self.state[1][1] == 1:
                print("Congrats! Player 1 Wins!")
            if self.state[1][1] == 2:
                print("Congrats! Player 2 Wins!")
            return True

        return False

    def isDraw(self):
        for row in range(3):
            for col in range(3):
                if self.state[row][col] == 0:
                    return False
        return True
