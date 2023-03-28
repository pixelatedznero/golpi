from ctypes import *
from enum import IntEnum

try:
    __golpi_lib = CDLL("../../build/golpi.so")
except:
    try:
        __golpi_lib = CDLL("build/golpi.so")
    except:
        raise Exception("Failed to load Golpi dynamic library.")

class GolpiCBoard(Structure):
    _fields_ = [("raw_data", c_char_p),
                ("x_dim", c_uint32),
                ("y_dim", c_uint32),
                ("border_mode", c_int32)]

GolpiCBoardP = POINTER(GolpiCBoard)

BORDER_MODE_TRANSPARENT = 0

_golpi_c_create_board = __golpi_lib.golpi_board_create
_golpi_c_create_board.restype = GolpiCBoard

_golpi_c_index_board = __golpi_lib.golpi_board_index
_golpi_c_index_board.restype = c_char

_golpi_c_index_board_ref = __golpi_lib.golpi_board_index_ref
_golpi_c_index_board_ref.restype = c_char_p

_golpi_c_check_board_zero = __golpi_lib.golpi_board_check_zero
_golpi_c_check_board_zero.restype = c_uint8

_golpi_c_surrounding_cells = __golpi_lib.golpi_board_active_surrounding_cells
_golpi_c_surrounding_cells.restype = c_uint8

_golpi_c_simulate_board = __golpi_lib.golpi_board_simulate
_golpi_c_simulate_board.restype = None

_golpi_c_print_board = __golpi_lib.golpi_board_print
_golpi_c_print_board.restype =  None

def golpi_c_create_board(raw_data: c_char_p, x_dim: c_uint32, y_dim: c_uint32, border_mode: c_int32) -> GolpiCBoard:
    return _golpi_c_create_board(raw_data, x_dim, y_dim, border_mode)

def golpi_c_index_board(board: GolpiCBoardP, x: c_uint32, y: c_uint32) -> c_char:
    return _golpi_c_index_board(board, x, y)

def golpi_c_index_board_ref(board: GolpiCBoardP, x: c_uint32, y: c_uint32) -> c_char_p:
    return _golpi_c_index_board_ref(board, x, y)

def golpi_c_check_board_zero(board: GolpiCBoardP) -> bool:
    return _golpi_c_check_board_zero(board)

def golpi_c_surrounding_cells(board: GolpiCBoardP, cell_x: c_uint32, cell_y: c_uint32) -> c_uint8:
    return _golpi_c_surrounding_cells(board, cell_x, cell_y)

def golpi_c_simulate_board(board: GolpiCBoardP) -> None:
    _golpi_c_simulate_board(board)

def golpi_c_print_board(board: GolpiCBoardP) -> None:
    _golpi_c_print_board(board)
