ENCODED_MOVES = {
    "P": ["n1", "n2_0", "ne1_x", "nw1_x"],
}


def sum_locations(location, direction):
    #g4, n1
    new_number = None
    if direction[0] == "n":
        new_number = int(location[-1]) + int(direction[-1])

    return f"{location[0]}{new_number}"


def get_valid_moves(board, piece):
    color = piece[0]
    piece_name = piece[2]
    location = piece[-2:]

    encoded_moves = ENCODED_MOVES[piece_name]

    new_location = sum_locations(location, encoded_moves[0])

    return [f"{piece}{new_location}"]
