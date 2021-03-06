def create_empty_board():
    return {
        "a": {
            "1": None,
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": None,
            "7": None,
            "8": None,
        },
        "b": {
            "1": None,
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": None,
            "7": None,
            "8": None,
        },
        "c": {
            "1": None,
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": None,
            "7": None,
            "8": None,
        },
        "d": {
            "1": None,
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": None,
            "7": None,
            "8": None,
        },
        "e": {
            "1": None,
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": None,
            "7": None,
            "8": None,
        },
        "f": {
            "1": None,
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": None,
            "7": None,
            "8": None,
        },
        "g": {
            "1": None,
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": None,
            "7": None,
            "8": None,
        },
        "h": {
            "1": None,
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": None,
            "7": None,
            "8": None,
        },
    }


def __place_piece(board, piece, coordinates):
    board[coordinates[0]][coordinates[1]] = piece
    return board


def move_piece(board, move):
    piece = move[0:5]
    next_location = move[5:7]

    # TODO: validate move

    return __place_piece(board, piece, next_location)


empty_board = create_empty_board()
print(move_piece(empty_board, "w_Pg4g5"))
