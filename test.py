from lib import simulation, utils

sim = simulation.Simulation()
util = utils.Utils()

pattern = [[0,0,0,0,0,0,],
           [0,1,1,0,0,0,],
           [0,1,1,0,0,0,],
           [0,0,0,1,1,0,],
           [0,0,0,1,1,0,],]

util.animategif(pattern, 10, "animation")