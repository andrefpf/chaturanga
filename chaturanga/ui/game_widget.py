from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)
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
        self.player_label = QLabel("JOGAM AS BRANCAS.")
        self.info_label = QLabel("")
        self.restart_button = QPushButton("Começar um novo jogo")

        self.player_label.setStyleSheet("font-weight: bold")

        self.restart_button.clicked.connect(self.restart_game)
        menu_layout = QVBoxLayout()
        menu_layout.addWidget(self.player_label)
        menu_layout.addWidget(self.restart_button)
        menu_layout.addWidget(self.info_label)
        menu_layout.setSpacing(25)

        self.menu_widget = QWidget()
        self.menu_widget.setLayout(menu_layout)
        self.player_label.setAlignment(Qt.AlignCenter)
        self.info_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.board_widget)
        layout.addWidget(self.menu_widget)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
        self.board_widget.update_board()  # To start with the sizes corrected
        self.set_visualization_player_color(Color.WHITE)
        self.show()

    def set_visualization_player_color(self, color):
        if color == Color.WHITE:
            self.player_label.setText("JOGAM AS BRANCAS.")
        else:
            self.player_label.setText("JOGAM AS PRETAS.")

    def clear_info_text(self):
        self.info_label.setText("")

    def restart_game(self):
        self.game.restart_game()
        self.last_piece = None
        self.board_widget.clear_highlights()
        self.board_widget.update_board()
        self.clear_info_text()

    def square_clicked_callback(self, row, col):
        clicked_square = self.game.board.get_square(row, col)

        if self.last_piece is None:
            self.choose_piece(clicked_square)
        else:
            self.move_choosen_piece(clicked_square)

    def set_last_piece(self, piece):
        self.last_piece = piece

    def choose_piece(self, target):
        if target.piece is None:
            self.clear_info_text()
            return

        if target.piece.color != self.game.current_color():
            self.info_label.setText("Escolha uma peça da sua cor")
            return

        self.set_last_piece(target.piece)
        self.board_widget.clear_highlights()
        self.board_widget.highlight_square_red(target.row, target.col)
        self.board_widget.highlight_movements(target.row, target.col)
        self.clear_info_text()

    def clear_last_piece(self):
        self.last_piece = None

    def move_choosen_piece(self, target):
        origin = self.last_piece.position
        self.clear_info_text()

        try:
            self.game.make_movement(origin, target)

        except InvalidMovement as error:
            self.info_label.setText(str(error))

        except InvalidPosition as error:
            self.info_label.setText(str(error))

        self.clear_last_piece()
        self.board_widget.clear_highlights()
        self.board_widget.update_board()

        if self.game.match_finished():
            self.show_winner()
        else:
            color = self.game.current_color()
            self.set_visualization_player_color(color)

    def show_winner(self):
        msg = QMessageBox()
        msg.addButton("Sim", QMessageBox.YesRole)
        msg.addButton("Não", QMessageBox.NoRole)

        winner = self.game.get_winner()
        if winner == Color.WHITE:
            msg.setText("VITÓRIA DAS BRANCAS!")
        elif winner == Color.BLACK:
            msg.setText("VITÓRIA DAS PRETAS!")
        else:
            return

        msg.setInformativeText("Deseja iniciar uma nova partida?")
        msg.setWindowTitle("Vitória!")
        should_exit = msg.exec()

        if should_exit:
            exit()
        else:
            self.restart_game()
