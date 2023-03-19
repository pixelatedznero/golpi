#import golpi, time
from ctypes import *

golpi_c_functions = CDLL("build/optimizedsim.so")
test_board = b'      *        ***                *                     *              *       ***                 *'

golpi_c_functions.update_board(test_board)
golpi_c_functions.print_board(test_board)


"""

- (converter 1d to 2d)
- python board object to 
- addpattern

"""




# times = []

# for i in range(5):
#     before = time.time()

#     board = golpi.createboard((100,100))
#     for i in range(20):
#         board.add([[1,1,1]], (i,i))

#     board.simulate(500)

#     times.append(time.time()-before)

# print(sum(times)/len(times))