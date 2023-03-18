import golpi

board = golpi.createboard((10,10))
board.add([[1,1,1]], (4,2))

board.simulate(1)

print(board.now)