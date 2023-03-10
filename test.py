import time

from lib import simulation as sim, utils, simslow

# sim = simulation.Simulation()
util = utils.Utils()

# zz = sim.run(sim.createboard(sim.convert2twod([0,0,0,0,0,
#                                                 0,1,1,1,1,
#                                                 1,0,0,0,1,
#                                                 0,0,0,0,1,
#                                                 1,0,0,1,0],5), 
#                               boardsize=(20,20)),
#              12)

# for i in range(len(zz)):
#     for x in range(len(zz[i])):
#         if zz[i][x] == 1:
#             zz[i][x] ="■"
#         else:
#             zz[i][x] =" "

# print(zz)

#check1 = util.checks.Checks(sim.run(sim.createboard(sim.convert2twod([0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,0],5)), 20, fullexport=True))
 
#print(check1.distance())

iters = 90

beforetime = time.time()
sim.run(sim.createboard(sim.convert2twod([1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 
                        1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 
                        1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 
                        0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 
                        1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 
                        1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 
                        1, 1, 1, 0, 1, 0, 1, 1, 0, 0],10)), iters, fullexport=True)

print(time.time() - beforetime)

beforetime = time.time()
sim.run(simslow.createboard(sim.convert2twod([1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 
                        1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 
                        1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 
                        0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 
                        1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 
                        1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 
                        1, 1, 1, 0, 1, 0, 1, 1, 0, 0],10)), iters, fullexport=True)

print(time.time() - beforetime)