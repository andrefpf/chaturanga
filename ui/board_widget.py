
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class BoardSquareWidget(QLabel):
    def __init__(self, QLabel, parent=None):
        super().__init__(parent)
        self.resize(60, 60)
        
        self.setStyleSheet('background-color: rgb(255,0,0)')

        self.show()

class BoardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.load_imgs()
        self.create_main_grid()

        # lb = QLabel(self)
        # pixmap = QPixmap('sprites/white_gaja.png')
        # lb.resize(100, 100)
        # lb.setPixmap(pixmap.scaled(lb.size(), Qt.IgnoreAspectRatio))

        self.show()

    def load_imgs(self):
        self.imgs = {
            'black_ashwa'   : QPixmap('sprites/black_ashwa.png'),
            'black_gaja'    : QPixmap('sprites/black_gaja.png'),
            'black_mantri'  : QPixmap('sprites/blackmantria.png'),
            'black_padati'  : QPixmap('sprites/black_padati.png'),
            'black_raja'    : QPixmap('sprites/black_raja.png'),
            'black_ratha'   : QPixmap('sprites/black_ratha.png'),
            
            'white_ashwa'   : QPixmap('sprites/white_ashwa.png'),
            'white_gaja'    : QPixmap('sprites/white_gaja.png'),
            'white_mantri'  : QPixmap('sprites/whitemantria.png'),
            'white_padati'  : QPixmap('sprites/white_padati.png'),
            'white_raja'    : QPixmap('sprites/white_arajapng'),
            'white_ratha'   : QPixmap('sprites/white_ratha.png'),
        }

    def create_main_grid(self):
        self.grid = QGridLayout(self)

        for i in range(8):
            for j in range(8):
                # lb = QLabel(self)
                # lb.resize(50, 50)
                # lb.setPixmap(pixmap.scaled(lb.size(), Qt.IgnoreAspectRatio))
                pixmap = self.imgs['black_raja']
                square = BoardSquareWidget(self)
                square.setPixmap(pixmap.scaled(square.size() * 0.5, Qt.IgnoreAspectRatio))
                self.grid.addWidget(square, i, j)

        self.setLayout(self.grid)