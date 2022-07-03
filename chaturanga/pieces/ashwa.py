from chaturanga.pieces import Piece


class Ashwa(Piece):
    def get_possible_movements(self, board):
        all_movements = [
            (self.position.row+1, self.position.col+2),
            (self.position.row+1, self.position.col-2),
            (self.position.row-1, self.position.col+2),
            (self.position.row-1, self.position.col-2),
            (self.position.row+2, self.position.col+1),
            (self.position.row+2, self.position.col-1),
            (self.position.row-2, self.position.col+1),
            (self.position.row-2, self.position.col-1),
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
        