from chaturanga.pieces.piece import Piece


class Ratha(Piece):
    def get_possible_movements(self, board):
        valid_movements = []

        row = self.position.row
        col = self.position.col
        while row > 0:
            row -= 1
            square = board.get_square(row, col)
            if not square.has_piece():
                valid_movements.append(square)
            elif square.piece.color != self.color:
                valid_movements.append(square)
                break
            elif square.piece.color == self.color:
                break

        row = self.position.row
        col = self.position.col
        while row < 7:
            row += 1
            square = board.get_square(row, col)
            if not square.has_piece():
                valid_movements.append(square)
            elif square.piece.color != self.color:
                valid_movements.append(square)
                break
            elif square.piece.color == self.color:
                break

        row = self.position.row
        col = self.position.col
        while col > 0:
            col -= 1
            square = board.get_square(row, col)
            if not square.has_piece():
                valid_movements.append(square)
            elif square.piece.color != self.color:
                valid_movements.append(square)
                break
            elif square.piece.color == self.color:
                break

        row = self.position.row
        col = self.position.col
        while col < 7:
            col += 1
            square = board.get_square(row, col)
            if not square.has_piece():
                valid_movements.append(square)
            elif square.piece.color != self.color:
                valid_movements.append(square)
                break
            elif square.piece.color == self.color:
                break

        return valid_movements
