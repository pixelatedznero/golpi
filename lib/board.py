try:
    from lib import optimisedsim as opt
except:
    import optimisedsim as opt

class Board:

    def __init__(self, startboard):
        self.now = startboard
        self.history = [[[]]]
        self.fullhistory = [[[]]]


    def add(self, pattern: list, position=()):
        pass


    def simulate(self, iterations: int):
        self.history = opt.run(self.now, iterations, True)
        self.now = self.history[len(self.history)-1]
        for i in self.history:
            self.fullhistory.append(i)

