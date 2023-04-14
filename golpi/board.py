from .c_impl.golpi_c import *

class Board:
    def __init__(self, start_data: bytes, x_dim: int, y_dim: int, border_mode: int) -> None:
        self.current_board = golpi_c_create_board(start_data, x_dim, y_dim, border_mode)
        """Represents the current board as a Ctypes struct object"""
        self.latest_history = [start_data]
        """Saves the last state of the simulation as list of bytes"""
        self.full_history = [start_data]
        """Saves all states of the simulation as list of bytes"""

    def add(self, patternobject: tuple, position: tuple) -> None:
        """ Add a patter to the current board
        
        Parameters
        ----------
        patternobject: tuple
        - Specifies the pattern that must be added to the board and its x dimension, can be easily created using patterns.create()

        position: tuple
        - Specifies the position at wich the pattern originates in the current board (x position, y position)

        Returns
        -------
        None """

        if len(patternobject[0]) % patternobject[1] != 0:
            raise Exception("Given dimension doesn't fit given pattern.")
        elif patternobject[1] + position[0] > self.current_board.x_dim or len(patternobject[0])/patternobject[1] + position[1] > self.current_board.x_dim:
           raise Exception("Either the position or the size of the pattern will place it, at least partially, outside of the board.") 

        data = bytearray(self.current_board.raw_data)
        split_pattern = [patternobject[0][i:i+patternobject[1]] for i in range(0, len(patternobject[0]), patternobject[1])]

        for line in range(int(len(patternobject[0])/patternobject[1])):
            start = (position[1]*self.current_board.x_dim) + position[0] + (line*self.current_board.x_dim)
            for i in range(start, start+patternobject[1]):
                data[i] = split_pattern[line][i-start]

        self.current_board.raw_data = bytes(data)
        self.latest_history[len(self.latest_history)-1] = bytes(data)
        self.full_history[len(self.full_history)-1] = bytes(data)

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
            golpi_c_simulate_board(pointer(self.current_board))
            self.full_history.append(self.current_board.raw_data)
        self.latest_history = self.full_history[len(self.full_history) - 1]
    
    def display(self) -> None:
        golpi_c_print_board(pointer(self.current_board))
