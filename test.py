import golpi

raw_data = b'                          *          *       ***                                                    '
board = golpi.board.Board(raw_data, 10, 10, 0)
board.simulate(3395901)
board.display()
