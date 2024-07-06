from src.board import gameBoard
from src.Player import Player


def gameLogic(gameBoard: gameBoard, p1: Player, p2: Player):
    player_turn = 0
    while True:
        if gameBoard.isWin():
            break
        elif gameBoard.isDraw():
            break
        else:
            if player_turn == 0:
                move = p1.make_move()
            else:
                move = p2.make_move()
            if move > 9 or move < 1:
                print("Invalid Move, try again!")
            else:
                row, col = (move - 1) // 3, (move - 1) % 3
                if gameBoard.isEmpty(row, col):
                    gameBoard.update(row, col, player_turn)
                    player_turn = 1 - player_turn
                    print(gameBoard)
                else:
                    print("Oh, that position is already taken! Pick another!")
