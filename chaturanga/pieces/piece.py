from enum import Enum


class Color(Enum):
    WHITE = 0
    BLACK = 1


class Piece:
    def __init__(self, color, position=None):
        self.color = color
        self.position = position

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def get_possible_movements(self, board):
        return []

    def __repr__(self):
        name = self.__class__.__name__
        color = self.color
        row = self.position.row
        col = self.position.col
        return f"<{name} {color} at ({row}, {col})>"
