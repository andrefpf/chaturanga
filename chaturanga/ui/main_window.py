from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from chaturanga.ui.board_widget import BoardWidget
from chaturanga.ui.game_widget import GameWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.central_widget = GameWidget(self)
        self.setWindowTitle("Chaturanga")
        self.setCentralWidget(self.central_widget)
        self.show()
