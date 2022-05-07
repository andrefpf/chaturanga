from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from ui.board_widget import BoardWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(400,400)

        self.setStyleSheet('background-color: rgb(0,0,0)')
        self.board = BoardWidget(self)
        self.setCentralWidget(self.board)

        self.show()