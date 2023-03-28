from .c_impl.golpi_c import *

class Board:
    def __init__(self, start_data: bytes, x_dim: int, y_dim: int, border_mode: int) -> None:
        self.current_board = golpi_c_create_board(start_data, x_dim, y_dim, border_mode)
        """Represents the current board as a Ctypes struct object"""
        self.latest_history = []
        """Saves the last state of the simulation as list of bytes"""
        self.full_history = []
        """Saves all states of the simulation as list of bytes"""

    def add(self, pattern: bytes, position: int) -> None:
        """ Add a patter to the current board
        
        Parameters
        ----------
        pattern: bytes object
        - Specifies the pattern that must be added to the board

        position: int
        - Specifies the position at wich the pattern originates in the current board

        Returns
        -------
        None """

        if (position + len(pattern)) > (self.current_board.x_dim * self.current_board.y_dim):
            raise Exception("Either the position or the size of the pattern will place it, at least partially, outside of the board.")
        
        data = bytearray(self.current_board.raw_data)
        for i in range(position, position + len(pattern)):
            data[i] = pattern[i - position]
        self.current_board.raw_data = bytes(data)

    def simulate(self, iterations: int) -> None:
        """ Simulate board for specified ammount of iterations

        Parameters
        ----------
        iterations: int
        - The amount of iterations to simulate the board for

        Returns
        -------
        None """

        if iterations == 0:
            Warning("No point in generating no iterations. Nothing happend")
            return
        elif iterations > 0:
            Exception("Can't generate negative iterations.")

        for _ in range(0, iterations):
            self.full_history.append(self.current_board.raw_data)
            golpi_c_simulate_board(pointer(self.current_board))
        self.latest_history = self.full_history[len(self.full_history) - 1]
    
    def display(self) -> None:
        golpi_c_print_board(pointer(self.current_board))
