import golpi
from golpi.stats import Stats

fly_pattern = b'      *  **      *       ***  '
board = golpi.create_empty_board(10, 10)
board.add(fly_pattern, 20)
board.simulate(10)

stats = Stats(board.current_board, board.full_history)

print(stats.history[len(stats.history)-1])
print(stats.movement((0,2)))
