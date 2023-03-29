import golpi
from golpi.stats import Stats

fly_pattern = b'      *          *       ***  '
board = golpi.create_empty_board(10, 100)
board.add(fly_pattern, 20)
board.simulate(10_000)   #4.4s -> Still some room for opimizations
board.display()

# stats = Stats(board)
# stats.movement()

print(golpi.convert_to_2d(fly_pattern, 5))