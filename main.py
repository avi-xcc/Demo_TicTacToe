from src.Player import Player
from src.board import gameBoard, print_instructions_to_console
from src.gameLogic import gameLogic

if __name__ == '__main__':
    p1 = Player("X")
    p2 = Player("O")
    gBoard = gameBoard()

    print_instructions_to_console()
    print()
    gameLogic(gBoard, p1, p2)

