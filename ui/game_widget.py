from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ui.board_widget import BoardWidget
from chaturanga.game import Game


class GameWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.game = Game()

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
        self.show()