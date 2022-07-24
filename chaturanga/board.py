from chaturanga.square import Square
from chaturanga.pieces import Ashwa, Gaja, Mitri, Padati, Raja, Ratha, Color
from chaturanga.errors import InvalidPosition


class Board:
    def __init__(self):
        self.squares = self.create_squares()
        self.set_initial_state()

    def move(self, origin, target):
        """
        Moves a piece on the board without caring about the rules.
        """
        piece = origin.get_piece()
        target.set_piece(piece)
        origin.set_piece(None)

    def create_squares(self):
        squares = []
        for i in range(8):
            row = []
            for j in range(8):
                s = Square(i, j, None)
                row.append(s)
            squares.append(row)
        return squares

    def get_square(self, row, col):
        if not (0 <= row < 8):
            raise InvalidPosition("Rows should be in the interval [0-8]")

        if not (0 <= col < 8):
            raise InvalidPosition("Columns should be in the interval [0-8]")

        return self.squares[row][col]

    def set_initial_state(self):
        """
        Puts every piece in the correct place to start the game.
        """

        first_row_order = [
            Ratha,
            Ashwa,
            Gaja,
            Raja,
            Mitri,
            Gaja,
            Ashwa,
            Ratha,
        ]

        for square in self:
            square.delete_piece()

        for i, PieceClass in enumerate(first_row_order):
            piece = PieceClass(Color.BLACK)
            self.get_square(0, i).set_piece(piece)

        for i in range(8):
            piece = Padati(Color.BLACK)
            self.get_square(1, i).set_piece(piece)

        for i, PieceClass in enumerate(first_row_order):
            piece = PieceClass(Color.WHITE)
            self.get_square(7, i).set_piece(piece)

        for i in range(8):
            piece = Padati(Color.WHITE)
            self.get_square(6, i).set_piece(piece)

    def __iter__(self):
        list_squares = []
        for row in self.squares:
            for square in row:
                list_squares.append(square)
        return iter(list_squares)
