import golpi
from golpi.stats import Stats

fly_pattern = b'      *          *       ***  '
board = golpi.create_empty_board(10, 100)
board.add(fly_pattern, (0, 2))
board.simulate(10_000)
board.display()

# stats = Stats(board)
# stats.movement()

print(golpi.convert_to_2d(fly_pattern, 5))