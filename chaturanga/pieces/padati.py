from chaturanga.pieces import Piece, Color

class Padati(Piece):
    def get_possible_movements(self, board):
        valid_movements = []

        if self.color == Color.BLACK:
            row = self.position.row + 1
            col = self.position.col
            if  (0 <= row < 8) and (0 <= col < 8):
                square = board.get_square(row, col)
                if not square.has_piece():
                    valid_movements.append(square)

            row = self.position.row + 1
            col = self.position.col - 1
            if  (0 <= row < 8) and (0 <= col < 8):
                square = board.get_square(row, col)
                if square.has_piece() and (square.piece.color != self.color):
                    valid_movements.append(square)

            row = self.position.row + 1
            col = self.position.col + 1
            if  (0 <= row < 8) and (0 <= col < 8):
                square = board.get_square(row, col)
                if square.has_piece() and (square.piece.color != self.color):
                    valid_movements.append(square)

        elif self.color == Color.WHITE:
            row = self.position.row - 1
            col = self.position.col
            if  (0 <= row < 8) and (0 <= col < 8):
                square = board.get_square(row, col)
                if not square.has_piece():
                    valid_movements.append(square)

            row = self.position.row - 1
            col = self.position.col - 1
            if  (0 <= row < 8) and (0 <= col < 8):
                square = board.get_square(row, col)
                if square.has_piece() and (square.piece.color != self.color):
                    valid_movements.append(square)

            row = self.position.row - 1
            col = self.position.col + 1
            if  (0 <= row < 8) and (0 <= col < 8):
                square = board.get_square(row, col)
                if square.has_piece() and (square.piece.color != self.color):
                    valid_movements.append(square)

        return valid_movements