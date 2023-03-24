from c_impl.golpi_c import *

class Board:
    def __init__(self, startboard):
        self.now = startboard
        """current board"""
        self.history = [[[]]]
        """history of the board for its last simulation"""
        self.fullhistory = [[[]]]
        """history since the board was created"""


    def add(self, pattern: list, position=()):
        """ initialize stats

        Parameters
        ----------
        pattern: 2D list
        - pattern that will be placed on the board

        position: tuple
        - position where pattern should be placed, centered if none

        Retruns
        -------
        Nothing"""

        self.now = opt.addpattern(pattern, self.now, list(position) if position != () else list(opt.centerposition(pattern, (len(self.now), len(self.now[0])))))


    def simulate(self, iterations: int):
        """ initialize stats

        Parameters
        ----------
        iterations: int
        - generations the current board should be simulated

        Retruns
        -------
        Nothing"""

        self.history = opt.run(self.now, iterations)
        self.now = self.history[len(self.history)-1]
        for i in self.history:
            self.fullhistory.append(i)

