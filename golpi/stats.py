from .board import Board

class Stats:
    def __init__(self, board: Board) -> None:
        self.board = board
        self.board.full_history = [[
                [1 if h[y * self.board.current_board.x_dim + x] == '*' or h[y * self.board.current_board.x_dim + x] == 42 else 0 
                for x in range(0, self.board.current_board.x_dim)] for y in range(0, len(h) // self.board.current_board.x_dim)
            ] for h in self.board.full_history]

    def movement(self, origin: tuple = (0, 0)) -> list:
        """ Computes the distance that every pixel has traveled in every direction

        Parameters
        ----------
        None

        Returns
        -------
        Vector of the total movement in x and y direction """

        movement_vector = [0, 0]

        for h in range(1, len(self.board.full_history)):
            current_history = self.board.full_history[h]
            last_history = self.board.full_history[h - 1]
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
        for h in self.board.full_history:
            if h[0] != 0 or h[0] != 1:
                h = [[1 if x == '*' else 0 for x in y] for y in h]
            
            total_alive_cells += sum([sum(y) for y in h])
        return total_alive_cells / len(self.board.full_history)

    def active_time(self) -> float:
        """ The amount of frames until all cells were dead

        Parameters
        ----------
        None

        Returns
        -------
        Frames until the board was dead or None if the board is still alive"""

        for i in range(0, len(self.board.full_history)):
            if sum([sum(y) for y in self.board.full_history[i]]) == 0:
                return i
        return None
