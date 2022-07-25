from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QMainWindow
from chaturanga.ui.game_widget import GameWidget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.central_widget = GameWidget(self)
        self.setWindowTitle("Chaturanga")
        self.setCentralWidget(self.central_widget)
        self.show()

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() & Qt.WindowMinimized:
                self.minimizeEvent(event)

    def minimizeEvent(self, event):
        """
        Checks if the mindow has minimized. It may be usefull.
        """
        pass
