import golpi, time, seagull

before = time.time()

board = golpi.createboard((100,100))
board.add(golpi.patterns.block)

board.simulate(500)

stats = golpi.initstats(board.history)
print(stats.distance())

print(time.time()-before)