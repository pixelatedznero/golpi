from golpi.c_impl.golpi_c import *

raw_data = b'      *        ***                *                     *              *       ***                 *'

board = golpi_c_create_board(raw_data, 10, 10, BORDER_MODE_TRANSPARENT)
golpi_c_print_board(pointer(board))