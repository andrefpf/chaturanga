from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from enum import Enum


class SquareTypes(Enum):
    NORMAL = 0
    HIGHLIGHT = 1
    REDLIGHT = 2


class BoardSquareWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(60, 60)
        
        self.set_type(SquareTypes.NORMAL)
        self.setAlignment(Qt.AlignCenter)
        self.show()

    def set_type(self, t):
        if t == SquareTypes.NORMAL:
            self.setStyleSheet(f'background-color: rgb(255,127,42)')
        elif t == SquareTypes.HIGHLIGHT:
            self.setStyleSheet(f'background-color: rgb(212,170,0)')
        elif t == SquareTypes.REDLIGHT:
            self.setStyleSheet(f'background-color: rgb(200,55,55)')
        else:
            pass

    def mouseReleaseEvent(self, event):
        self.set_type(SquareTypes.HIGHLIGHT)


class BoardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 400)
        self.setMaximumSize(400, 400)
        
        pal = QPalette()
        pal.setColor(QPalette.Window, Qt.black)
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        self.setStyleSheet('background-color:black')
        
        self.load_imgs()
        self.create_main_grid()

        self.show()
    
    def hasHeightForWidth(width):
        return True

    def load_imgs(self):
        self.imgs = {
            'empty'         : QPixmap(60,60),

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

    def create_main_grid(self):
        self.grid = QGridLayout(self)
        self.grid.setHorizontalSpacing(5)
        self.grid.setVerticalSpacing(5)

        for i in range(8):
            for j in range(8):
                square = BoardSquareWidget(self)
                self.grid.addWidget(square, i, j)

        self.setLayout(self.grid)

    def set_piece(self, x, y, piece):
        square = self.grid.itemAtPosition(x,y).widget()
        pixmap = self.imgs[piece]
        ratio = 0.7 if 'padati' in piece else 0.9
        pixmap = pixmap.scaled(square.size() * ratio, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        square.setPixmap(pixmap)

    def set_square_type(self, x, y, t):
        square = self.grid.itemAtPosition(x,y).widget()
        square.set_type(t)
