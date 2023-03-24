from c_impl.golpi_c import *
from stats import Stats

class Board:
    def __init__(self, start_data: bytes, x_dim: int, y_dim: int, border_mode: int) -> None:
        self.current_board = golpi_c_create_board(start_data, x_dim, y_dim, border_mode)
        """Represents the current board as a Ctypes struct object"""
        self.latest_history = []
        """Saves the last state of the simulation"""
        self.full_history = []
        """Saves all states of the simulation"""

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

        if((position + len(pattern)) > (self.current_board.x_dim * self.current_board.y_dim)):
            raise Exception("Pattern is too long to fit into current board.")
        
        for i in range(position, position + len(pattern)):
            self.current_board.raw_data[i] = pattern[i - position]

    def simulate(self, iterations: int) -> None:
        """ Simulate board for specified ammount of iterations

        Parameters
        ----------
        iterations: int
        - The amount of iterations to simulate the board for

        Returns
        -------
        None """

        for _ in range(0, iterations):
            self.full_history.append(self.current_board.raw_data)
            golpi_c_simulate_board(pointer(self.current_board))
        self.latest_history = self.full_history[len(self.full_history) - 1]

    def stats(self) -> Stats:
        return Stats(self.full_history, self.latest_history)
