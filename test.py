import golpi, time, seagull

times = []

for i in range(5):
    before = time.time()

    board = golpi.createboard((100,100))
    for i in range(20):
        board.add([[1,1,1]], (i,i))

    board.simulate(500)

    times.append(time.time()-before)

print(sum(times)/len(times))