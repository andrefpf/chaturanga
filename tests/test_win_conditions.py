from chaturanga.game import Game
from chaturanga.pieces import Color


def test_kings_death():
    moves = [
        ((7, 6), (5, 5)),
        ((1, 0), (2, 0)),
        ((5, 5), (3, 6)),
        ((2, 0), (3, 0)),
        ((3, 6), (1, 5)),
        ((3, 0), (4, 0)),
    ]

    game = Game()
    board = game.board

    for o, t in moves:
        o_row, o_col = o
        t_row, t_col = t
        origin = board.get_square(o_row, o_col)
        target = board.get_square(t_row, t_col)
        game.make_movement(origin, target)

        assert game.match_finished() is False
        assert game.get_winner() is None

    origin = board.get_square(1, 5)
    target = board.get_square(0, 3)
    game.make_movement(origin, target)

    assert game.match_finished() is True
    assert game.get_winner() == Color.WHITE


def test_army_decimated():
    moves = [
        ((6, 7), (5, 7)),
        ((1, 7), (2, 7)),
        ((5, 7), (4, 7)),
        ((2, 7), (3, 7)),
        ((6, 6), (5, 6)),
        ((0, 7), (2, 7)),
        ((5, 6), (4, 6)),
        ((2, 7), (2, 0)),
        ((6, 5), (5, 5)),
        ((2, 0), (6, 0)),
        ((5, 5), (4, 5)),
        ((6, 0), (7, 0)),
        ((6, 4), (5, 4)),
        ((7, 0), (7, 1)),
        ((5, 4), (4, 4)),
        ((7, 1), (7, 2)),
        ((7, 3), (6, 4)),
        ((7, 2), (7, 4)),
        ((6, 3), (5, 3)),
        ((7, 4), (7, 5)),
        ((5, 3), (4, 3)),
        ((7, 5), (7, 6)),
        ((6, 2), (5, 2)),
        ((7, 6), (7, 7)),
        ((5, 2), (4, 2)),
        ((7, 7), (4, 7)),
        ((6, 1), (5, 1)),
        ((4, 7), (4, 6)),
        ((5, 1), (4, 1)),
        ((4, 6), (4, 5)),
        ((4, 1), (3, 1)),
        ((4, 5), (4, 4)),
        ((3, 1), (2, 1)),
        ((4, 4), (4, 3)),
        ((2, 1), (1, 0)),
        ((4, 3), (4, 2)),
        ((1, 0), (0, 1)),
    ]

    game = Game()
    board = game.board

    for o, t in moves:
        o_row, o_col = o
        t_row, t_col = t
        origin = board.get_square(o_row, o_col)
        target = board.get_square(t_row, t_col)
        game.make_movement(origin, target)

        assert game.match_finished() is False
        assert game.get_winner() is None

    origin = board.get_square(0, 0)
    target = board.get_square(0, 1)
    game.make_movement(origin, target)

    assert game.match_finished() is True
    assert game.get_winner() == Color.BLACK
