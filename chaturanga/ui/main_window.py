from PyQt5.QtWidgets import QMainWindow
from chaturanga.ui.game_widget import GameWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.central_widget = GameWidget(self)
        self.setWindowTitle("Chaturanga")
        self.setCentralWidget(self.central_widget)
        self.show()
