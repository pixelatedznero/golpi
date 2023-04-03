from .utility import *
import copy

class Stats:
    def __init__(self, current_board, history: list) -> None:
        self.current_board = current_board

        for key, h in enumerate(history):
            history[key] = convert_binary_to_2d(h, current_board.x_dim)
        self.history = history


    def movement(self, origin: tuple = (0, 0)) -> list:
        """ Computes the distance that every pixel has traveled in every direction

        Parameters
        ----------
        None

        Returns
        -------
        List of tuples of vectors of the total movement in x and y direction """

        current = copy.deepcopy(self.history[len(self.history)-1])
        empty_rows = []
        changed_origin = list(origin)

        if origin[0] > self.current_board.x_dim or origin[1] > self.current_board.y_dim:
            raise Exception("Origin coordinates outside of board.")


        for key, y in enumerate(self.history[len(self.history)-1]):
            if sum(y) == 0:
                empty_rows.append(key)
                if len(empty_rows)-1 == key:
                    changed_origin[1] = changed_origin[1] - 1

        for i in reversed(empty_rows):
            current.pop(i)

        allvectors = {}

        for ykey, y in enumerate(current):
            for xkey, x in enumerate(y):
                if x == 1:
                    actual_ykey = ykey-(changed_origin[1]-origin[1])
                    allvectors[(xkey, actual_ykey)] = xkey + actual_ykey

        max_vectors = []
        max_distance = allvectors[max(allvectors)]
        for i in allvectors:
            if allvectors[i] == max_distance:
                max_vectors.append(i)
                
        return max_vectors



    def pixels_per_frame(self) -> float:
        """ Computes the average of alive pixels for all frames

        Parameters
        ----------
        None

        Returns
        -------
        Average of alive pixels for all frames """

        total_alive_cells = 0
        for h in self.history:
            total_alive_cells += sum([sum(y) for y in h])
        return total_alive_cells / len(self.history)

    def active_time(self) -> float:
        """ The amount of frames until all cells were dead

        Parameters
        ----------
        None

        Returns
        -------
        Frames until the board was dead or None if the board is still alive"""

        for i in range(0, len(self.history)):
            if sum([sum(y) for y in self.history[i]]) == 0:
                return i
        return None
