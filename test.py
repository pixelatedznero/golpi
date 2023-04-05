import golpi
from golpi.stats import Stats

fly_pattern = b'      *          *       ***  '
board = golpi.create_empty_board(10, 10)
board.add(fly_pattern, (0, 2))
board.simulate(1)
board.display()

stats = Stats(board.current_board, board.full_history)

print(board.full_history)
print(stats.movement((0,3)))
