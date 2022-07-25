class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def has_piece(self):
        return self.piece is not None

    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece
        if piece is not None:
            self.piece.position = self

    def delete_piece(self):
        self.piece = None

    def __repr__(self):
        if self.piece is None:
            return f"<Empty at ({self.row}, {self.col})>"
        else:
            return str(self.piece)
