from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from chaturanga.ui.board_widget import BoardWidget
from chaturanga.game import Game
from chaturanga.pieces.piece import Color
from chaturanga.errors import InvalidMovement, InvalidPosition


class GameWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.game = Game()
        self.last_piece = None

        self.board_widget = BoardWidget(self)
        self.player_label = QLabel("Jogam as Brancas.")
        self.info_label = QLabel("Nada de errado, apenas jogue.")
        self.restart_button = QPushButton("Começar um novo jogo")

        self.restart_button.clicked.connect(self.restart_game)
        menu_layout = QVBoxLayout()
        menu_layout.addWidget(self.player_label)
        menu_layout.addWidget(self.info_label)
        menu_layout.addWidget(self.restart_button)
        menu_layout.setSpacing(25)
        menu_layout.setAlignment(Qt.AlignCenter)

        self.menu_widget = QWidget()
        self.menu_widget.setLayout(menu_layout)
        self.player_label.setAlignment(Qt.AlignCenter)
        self.info_label.setAlignment(Qt.AlignCenter)

        layout = QHBoxLayout()
        layout.addWidget(self.board_widget)
        layout.addWidget(self.menu_widget)

        self.setLayout(layout)
        self.show()

    def restart_game(self):
        self.game.restart_game()
        self.last_piece = None
        self.board_widget.clear_highlights()
        self.board_widget.update_board()
        self.info_label.setText("")

    def square_clicked_callback(self, row, col):
        clicked_square = self.game.board.get_square(row, col)

        if self.last_piece is None:
            self.choose_piece(clicked_square)
        else:
            self.move_choosen_piece(clicked_square)

    def choose_piece(self, target):
        if target.piece is None:
            self.info_label.setText("")
            return

        if target.piece.color != self.game.current_color():
            self.info_label.setText("Escolha uma peça da sua cor")
            return

        self.last_piece = target.piece
        self.board_widget.clear_highlights()
        self.board_widget.highlight_square_red(target.row, target.col)
        self.board_widget.highlight_movements(target.row, target.col)
        self.info_label.setText("")

    def move_choosen_piece(self, target):
        origin = self.last_piece.position

        try:
            origin = self.last_piece.position
            self.game.make_movement(origin, target)
            self.info_label.setText("")

        except InvalidMovement as error:
            self.info_label.setText(str(error))

        except InvalidPosition as error:
            self.info_label.setText(str(error))

        self.last_piece = None
        self.board_widget.clear_highlights()
        self.board_widget.update_board()

        if self.game.match_finished():
            self.show_winner()
        else:
            if self.game.current_color() == Color.WHITE:
                self.player_label.setText("Jogam as Brancas.")
            elif self.game.current_color() == Color.BLACK:
                self.player_label.setText("Jogam as Pretas.")
            else:
                raise ValueError("Unknown current player.")

    def show_winner(self):
        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        if self.game.get_winner() == Color.WHITE:
            msg.setText("VITÓRIA DAS BRANCAS!")
        elif self.game.get_winner() == Color.BLACK:
            msg.setText("VITÓRIA DAS PRETAS!")
        else:
            return

        msg.setInformativeText("Deseja iniciar uma nova partida?")
        msg.setWindowTitle("Vitória!")
        ret = msg.exec()

        if ret == QMessageBox.Yes:
            self.restart_game()
        else:
            exit()
