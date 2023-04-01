from .utility import *

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
        Vector of the total movement in x and y direction """

        movement_vector = [0, 0]

        for h in range(1, len(self.history)):
            current_history = self.history[h]
            last_history = self.history[h - 1]
            if len(current_history) != len(last_history):
                raise Exception("Histories stored inside of Board object have different sizes.")

            diff_history = [
                [last_history[y][x] - current_history[y][x] for x in range(0, len(current_history[y]))] 
                for y in range(0, len(current_history))
            ]

            row_sum = [sum(y) for y in diff_history]
            column_sum = []
            for i in range(0, len(diff_history[0])):
                temp = 0
                for j in range(0, len(diff_history)):
                    temp += diff_history[j][i]
                column_sum.append(temp)

            print(f"({row_sum}|{column_sum})")

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
