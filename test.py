import golpi
from golpi.stats import Stats

fly_pattern = golpi.patterns.create(b' *    * *** ', 4)
board = golpi.create_empty_board(10, 10)
board.add(fly_pattern, (2, 2))
board.display()

print(golpi.convert_binary_to_2d(board.full_history[0], 10))
