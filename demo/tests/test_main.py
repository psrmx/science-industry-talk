import pytest
from bccn_chess.main import create_empty_board, __place_piece
from bccn_chess.moves import get_valid_moves


@pytest.fixture
def empty_board():
    return create_empty_board()


def test_places_piece_in_board(empty_board):
    piece = "w_Q"
    coordinate = "g4"

    updated_board = __place_piece(empty_board, piece, coordinate)

    assert updated_board["g"]["4"] == piece


def test_lonely_pawn_steps_foreward(empty_board):
    pawn = "w_Pg4"
    board = __place_piece(empty_board, pawn, "g4")

    valid_moves = get_valid_moves(board, pawn)

    assert valid_moves == ["w_Pg4g5"]



def xtest_valid_moves_in_board_with_two_pawns(empty_board):
    board = __place_piece(empty_board, "w_P", "g4")
    board = __place_piece(board, "b_P", "g5")

    actual = get_valid_moves(board, "w_P")

    assert actual == []
