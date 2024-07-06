class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self):
        try:
            print(f"{self.symbol}'s Turn")
            move = int(input("Enter a location to move to : "))
            return move
        except Exception as e:
            print("Invalid Move, please select a value between 0 and 9")
            return -1

    def get_symbol(self):
        return self.symbol
