import pytest
from bccn_chess.main import create_empty_board, __place_piece


@pytest.fixture
def empty_board():
    return create_empty_board()


def test_piece_is_placed_in_board(empty_board):
    piece = ["white", "queen"]
    actual = __place_piece(empty_board, piece, "g4")

    assert actual["g"]["4"] == piece
