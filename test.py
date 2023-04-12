import golpi
from golpi.stats import Stats

fly_pattern = golpi.patterns.create(b' *    * *** ', 4)
board = golpi.create_empty_board(20, 20)
board.add(golpi.patterns.Others.generate_crown(), (0, 0))
for i in range(15):
    board.simulate(1)
    board.display()
    print("----------")

