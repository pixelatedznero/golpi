import golpi
from golpi.stats import Stats
import time

fly_pattern = golpi.patterns.create(b'* * ** * **   *  * * * * * *    * ****   *   ***   *** *   *  * * * * * *    * ****   *   ***   *** ', 10)
board = golpi.create_empty_board(100, 100)
board.add(fly_pattern, (5, 5))

before = time.time()
board.simulate(400)
board.display()
print(time.time()-before)
