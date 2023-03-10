try:
    from lib import optimisedsimulation as opt
except:
    import optimisedsimulation as opt


def convert2twod(inputlist, length):
    return opt.convert2twod(inputlist, length)

def centerpattern(pattern, boardsize):
    return opt.centerpattern(pattern, boardsize)

def createboard(pattern, boardsize=(100,100), patternposition=None):
    return opt.createboard(pattern, boardsize, patternposition)

def run(board, iterations, fullexport=False):
    return opt.run(board, iterations, fullexport)