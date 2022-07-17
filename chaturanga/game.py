from chaturanga.board import Board
from chaturanga.pieces import Color, Raja
from chaturanga.errors import InvalidMovement, InvalidPosition


class Game:
    def __init__(self):
        self.board = Board()
        self.restart_game()

    def restart_game(self):
        self.board.set_initial_state()
        self._turn = 0
        self._winner = None
        self._match_finished = False

    def match_finished(self):
        return self._match_finished

    def current_color(self):
        if self._turn % 2 == 0:
            return Color.WHITE
        else:
            return Color.BLACK

    def increment_turn_counter(self):
        self._turn += 1

    def make_movement(self, origin, target):
        """
        Attempts to make a movement. If it is not a valid one, throws an error.
        """
        self.evaluate_movement(origin, target)
        self.board.move(origin, target)
        self.evaluate_promotion(target.piece)
        self.evaluate_winning_condition()
        self.increment_turn_counter()

    def evaluate_movement(self, origin, target):
        if not origin in self.board:
            raise InvalidPosition("Posição fora do tabuleiro")

        if not target in self.board:
            raise InvalidPosition("Posição fora do tabuleiro")

        if not origin.has_piece():
            raise InvalidMovement("Nenhuma peça selecionada")

        if origin.get_piece().color != self.current_color():
            raise InvalidMovement("Escolha uma peça da cor certa")

        movements = origin.get_piece().get_possible_movements(self.board)
        if target not in movements:
            raise InvalidMovement("Jogada inválida")

    def get_winner(self):
        return self._winner

    def evaluate_promotion(self, piece):
        NotImplemented

    def evaluate_winning_condition(self):
        self._check_kings_death()
        self._check_army_decimated()

    def _check_kings_death(self):
        contains_raja = lambda x: x.has_piece() and isinstance(x.get_piece(), Raja)
        rajas = [square for square in self.board if contains_raja(square)]

        if len(rajas) == 2:
            return

        self._match_finished = True
        self._winner = rajas[0].get_piece().color

    def _check_army_decimated(self):
        NotImplemented
