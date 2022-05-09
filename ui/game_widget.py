from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from ui.board_widget import BoardWidget


class GameWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.board_widget = BoardWidget(self)
        self.player_label = QLabel('Jogam as Brancas.')
        self.info_label = QLabel('Nada de errado, apenas jogue.')
        self.restart_button = QPushButton('Começar um novo jogo')

        menu_layout = QVBoxLayout()
        menu_layout.addWidget(self.player_label)
        menu_layout.addWidget(self.info_label)
        menu_layout.addWidget(self.restart_button)
        self.menu_widget = QWidget()
        self.menu_widget.setLayout(menu_layout)

        menu_layout.setSpacing(25)
        menu_layout.setAlignment(Qt.AlignCenter)
        self.player_label.setAlignment(Qt.AlignCenter)
        self.info_label.setAlignment(Qt.AlignCenter)

        layout = QHBoxLayout()
        layout.addWidget(self.board_widget)
        layout.addWidget(self.menu_widget)
        self.setLayout(layout)

        self.set_initial_board()
        self.show()
    
    def set_initial_board(self):
        self.board_widget.set_piece(0, 0, 'black_ratha')
        self.board_widget.set_piece(0, 1, 'black_ashwa')
        self.board_widget.set_piece(0, 2, 'black_gaja')
        self.board_widget.set_piece(0, 3, 'black_raja')
        self.board_widget.set_piece(0, 4, 'black_mitri')
        self.board_widget.set_piece(0, 5, 'black_gaja')
        self.board_widget.set_piece(0, 6, 'black_ashwa')
        self.board_widget.set_piece(0, 7, 'black_ratha')

        for i in range(8):
            self.board_widget.set_piece(1, i, 'black_padati')

        self.board_widget.set_piece(7, 0, 'white_ratha')
        self.board_widget.set_piece(7, 1, 'white_ashwa')
        self.board_widget.set_piece(7, 2, 'white_gaja')
        self.board_widget.set_piece(7, 3, 'white_mitri')
        self.board_widget.set_piece(7, 4, 'white_raja')
        self.board_widget.set_piece(7, 5, 'white_gaja')
        self.board_widget.set_piece(7, 6, 'white_ashwa')
        self.board_widget.set_piece(7, 7, 'white_ratha')

        for i in range(8):
            self.board_widget.set_piece(6, i, 'white_padati')