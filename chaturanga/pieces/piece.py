from enum import Enum 


class Color(Enum):
    WHITE = 0
    BLACK = 1


class Piece:
    def __init__(self, color, position=None):
        self.color = color
        self.position = position

    def get_possible_movements(self, board):
        row = self.position.row
        col = self.position.col
        if row > 7:
            return []
        return [board.get_square(self.position.row+1, self.position.col)]