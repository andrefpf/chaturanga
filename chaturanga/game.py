from chaturanga.board import Board
from chaturanga.pieces import Color, Raja, Padati, Mitri
from chaturanga.errors import InvalidMovement, InvalidPosition


class Game:
    def __init__(self):
        self.board = Board()
        self.restart_game()

    def restart_game(self):
        self.board.set_initial_state()
        self._turn = 0
        self._player = Color.WHITE
        self._winner = None
        self._match_finished = False

    def match_finished(self):
        return self._match_finished

    def current_color(self):
        return self._player

    def get_winner(self):
        return self._winner

    def make_movement(self, origin, target):
        """
        Attempts to make a movement. If it is not a valid one, throws an error.
        """
        self._evaluate_movement(origin, target)
        self.board.move(origin, target)
        self._evaluate_promotion(target.piece)
        self._evaluate_winning_condition()

        if not self.match_finished():
            self._increment_turn_counter()

    def _increment_turn_counter(self):
        self._turn += 1

        if self._turn % 2 == 0:
            self._player = Color.WHITE
        else:
            self._player = Color.BLACK

    def _evaluate_movement(self, origin, target):
        if origin not in self.board:
            raise InvalidPosition("Posição fora do tabuleiro")

        if target not in self.board:
            raise InvalidPosition("Posição fora do tabuleiro")

        if not origin.has_piece():
            raise InvalidMovement("Nenhuma peça selecionada")

        if origin.get_piece().color != self.current_color():
            raise InvalidMovement("Escolha uma peça da cor certa")

        movements = origin.get_piece().get_possible_movements(self.board)
        if target not in movements:
            raise InvalidMovement("Jogada inválida")

    def _evaluate_promotion(self, piece):
        if not isinstance(piece, Padati):
            return

        color = piece.get_color()
        pos = piece.get_position()
        row = pos.get_row()

        if (color == Color.WHITE and row == 0) or (color == Color.BLACK and row == 7):
            new_piece = Mitri(color)
            pos.set_piece(new_piece)

    def _evaluate_winning_condition(self):
        self._check_kings_death()
        self._check_army_decimated()

    def _check_kings_death(self):
        rajas = [
            square for square in self.board if isinstance(square.get_piece(), Raja)
        ]

        if len(rajas) == 1:
            self._match_finished = True
            self._winner = rajas[0].get_piece().color

    def get_black_pieces(self):
        def _has_black(square):
            return square.has_piece() and square.piece.color == Color.BLACK

        return list(filter(_has_black, self.board))

    def get_white_pieces(self):
        def _has_white(square):
            return square.has_piece() and square.piece.color == Color.WHITE

        return list(filter(_has_white, self.board))

    def set_winner(self, color):
        self._match_finished = True
        self._winner = color

    def _check_army_decimated(self):
        black_pieces = self.get_black_pieces()
        white_pieces = self.get_white_pieces()

        if len(black_pieces) <= 1:
            self.set_winner(Color.WHITE)

        if len(white_pieces) <= 1:
            self.set_winner(Color.BLACK)
