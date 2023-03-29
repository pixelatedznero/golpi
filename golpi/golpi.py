from .board import Board

def create_empty_board(x_dim: int, y_dim: int, border_mode: int = 0) -> Board:
    """ Create an empty board

    Parameters
    ----------
    x_dim: int
    - The row size of the empty board

    y_dim: int
    - The column size of the empty board

    border_mode: int = 0
    - The border_mode of the empty board

    Returns
    -------
    An empty board object with given dimensions and border mode """
    
    board = bytearray(b'')
    for _ in range(0, x_dim * y_dim):
        board += b' '
    return Board(bytes(board), x_dim, y_dim, border_mode)