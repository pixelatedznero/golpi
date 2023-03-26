import golpi

fly_pattern = b'      *          *       ***  '
board = golpi.golpi.create_empty_board(10, 100)
board.add(fly_pattern, 20)
board.simulate(1_000_000)   #4.4s -> Still some room for opimizations
board.display()