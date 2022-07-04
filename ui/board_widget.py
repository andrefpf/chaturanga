from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from enum import Enum
from chaturanga.pieces import *
from chaturanga.board import Board


class SquareHighlight(Enum):
    NORMAL = 0
    HIGHLIGHT = 1
    SELECTED = 2


class BoardSquareWidget(QLabel):
    def __init__(self, row, col, parent=None):
        super().__init__(parent)
        self.resize(60, 60)

        self.row = row
        self.col = col
        
        self.setAlignment(Qt.AlignCenter)
        self.show()

    def highlight(self, t):
        if t == SquareHighlight.NORMAL:
            self.setStyleSheet(f'background-color: rgb(255,127,42)')

        elif t == SquareHighlight.HIGHLIGHT:
            self.setStyleSheet(f'background-color: rgb(212,170,0)')

        elif t == SquareHighlight.SELECTED:
            self.setStyleSheet(f'background-color: rgb(200,55,55)')
        else:
            pass

    def mouseReleaseEvent(self, event):
        self.parent().square_clicked_callback(self.row, self.col)


class BoardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(500, 500)
        self.setMaximumSize(500, 500)
        
        self.board = self.parent().game.board
        self.last_piece = None

        pal = QPalette()
        pal.setColor(QPalette.Window, Qt.black)
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        self.setStyleSheet('background-color:black')
        
        self._load_imgs()
        self._create_main_grid()
        self.update_board()
        self.show()
    
    def hasHeightForWidth(width):
        '''
            Override method of QWidget.
        '''
        return True

    def _load_imgs(self):
        self.imgs = {
            'empty'         : QPixmap(10,10),

            'black_ashwa'   : QPixmap('sprites/black_ashwa.png'),
            'black_gaja'    : QPixmap('sprites/black_gaja.png'),
            'black_mitri'   : QPixmap('sprites/black_mitri.png'),
            'black_padati'  : QPixmap('sprites/black_padati.png'),
            'black_raja'    : QPixmap('sprites/black_raja.png'),
            'black_ratha'   : QPixmap('sprites/black_ratha.png'),
            
            'white_ashwa'   : QPixmap('sprites/white_ashwa.png'),
            'white_gaja'    : QPixmap('sprites/white_gaja.png'),
            'white_mitri'   : QPixmap('sprites/white_mitri.png'),
            'white_padati'  : QPixmap('sprites/white_padati.png'),
            'white_raja'    : QPixmap('sprites/white_raja.png'),
            'white_ratha'   : QPixmap('sprites/white_ratha.png'),
        }
        self.imgs['empty'].fill(Qt.transparent)

    def _create_main_grid(self):
        self.grid = QGridLayout(self)
        self.grid.setHorizontalSpacing(5)
        self.grid.setVerticalSpacing(5)

        for row in range(8):
            for col in range(8):
                square = BoardSquareWidget(row, col, parent=self)
                self.grid.addWidget(square, row, col)

        self.setLayout(self.grid)

    def set_piece(self, row, col, piece_name):
        '''
            Sets the correspondent image for the square of your choice.
        '''
        square_widget = self.grid.itemAtPosition(row, col).widget()
        pixmap = self.imgs[piece_name]
        ratio = 0.7 if 'padati' in piece_name else 0.9
        pixmap = pixmap.scaled(square_widget.size() * ratio, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        square_widget.setPixmap(pixmap)

    def clear_highlights(self):
        '''
            Sets all the highlighted squares to their original color.
        '''
        for i in range(8):
            for j in range(8):
                square = self.grid.itemAtPosition(i,j).widget()
                square.highlight(SquareHighlight.NORMAL)

    def highlight_square(self, row, col):
        '''
            Paints a square as yellow.
        '''
        square_widget = self.grid.itemAtPosition(row, col).widget()
        square_widget.highlight(SquareHighlight.HIGHLIGHT)

    def highlight_selected_square(self, row, col):
        '''
            Paints a square as red. 
        '''
        square_widget = self.grid.itemAtPosition(row, col).widget()
        square_widget.highlight(SquareHighlight.SELECTED)

    def highlight_movements(self, row, col):
        '''
            Paints as yellow all squares which is possible to reach from the specified position.
        '''
        clicked_square = self.board.get_square(row, col)

        if not isinstance(clicked_square.piece, Piece):
            return
        
        possible_movements = clicked_square.piece.get_possible_movements(self.board)
        
        for square in possible_movements:
            self.highlight_square(square.row, square.col)

    def update_board(self):
        '''
            Updates all piece images of the board widget according to the state of the actual board.
        '''
        self.clear_highlights()

        for square in self.board:
            if not isinstance(square.piece, Piece):
                self.set_piece(square.row, square.col, 'empty')
                continue

            piece = square.piece 
            piece_prefix = 'white_' if piece.color == Color.WHITE else 'black_'

            if isinstance(piece, Ashwa):
                piece_name = piece_prefix + 'ashwa'
                self.set_piece(square.row, square.col, piece_name)

            elif isinstance(piece, Gaja):
                piece_name = piece_prefix + 'gaja'
                self.set_piece(square.row, square.col, piece_name)

            elif isinstance(piece, Mitri):
                piece_name = piece_prefix + 'mitri'
                self.set_piece(square.row, square.col, piece_name)

            elif isinstance(piece, Padati):
                piece_name = piece_prefix + 'padati'
                self.set_piece(square.row, square.col, piece_name)

            elif isinstance(piece, Raja):
                piece_name = piece_prefix + 'raja'
                self.set_piece(square.row, square.col, piece_name)

            elif isinstance(piece, Ratha):
                piece_name = piece_prefix + 'ratha'
                self.set_piece(square.row, square.col, piece_name)

    def choose_piece(self, target):
        if target.piece is None:
            # TODO: Show warning on GUI
            return 

        # TODO: Evaluate if piece belongs to the current player

        self.last_piece = target.piece
        self.clear_highlights()
        self.highlight_selected_square(target.row, target.col)
        self.highlight_movements(target.row, target.col)
    
    def move_choosen_piece(self, target):
        origin = self.last_piece.position

        if self.last_piece is None:
            # TODO: Show warning on GUI
            return

        # TODO: Evaluate if 

        movements = self.last_piece.get_possible_movements(self.board)
        if target in movements:
            self.board.move(self.last_piece.position, target)

        # TODO: Evaluate win condition
        # TODO: Increment turn counter

        self.last_piece = None
        self.clear_highlights()
        self.update_board()

    def square_clicked_callback(self, row, col):
        '''
            Function callback for everytime a square is clicked.
        '''

        # TODO: Evaluate if match is ongoing

        clicked_square = self.board.get_square(row, col)

        if self.last_piece is None:
            self.choose_piece(clicked_square)
        else:
            self.move_choosen_piece(clicked_square)
