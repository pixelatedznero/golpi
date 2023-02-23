from lib import simulation, utils

sim = simulation.Simulation()
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

check1 = util.checks.Checks(sim.run(sim.createboard(sim.convert2twod([0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,0],5)), 20, fullexport=True))
 
print(check1.distance())

util.animategif(sim.convert2twod([0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,0],5), 20, "animation", )