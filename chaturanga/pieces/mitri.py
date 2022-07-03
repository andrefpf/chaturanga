from chaturanga.pieces.piece import Piece


class Mitri(Piece):
    def get_possible_movements(self, board):
        row = self.position.row
        col = self.position.col

        all_movements = [
            (row+1, col+1),
            (row+1, col-1),
            (row-1, col+1),
            (row-1, col-1),
        ]

        valid_movements = []
        for row, col in all_movements:
            if not (0 <= row < 8):
                continue
                
            if not (0 <= col < 8):
                continue 

            square = board.get_square(row, col)

            if not square.has_piece():
                valid_movements.append(square)
            
            elif square.piece.color != self.color:
                valid_movements.append(square)

        return valid_movements
