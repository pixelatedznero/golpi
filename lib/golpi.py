try:
    from lib import optimisedsim as opt, board, stats, patterns
except:
    import optimisedsim as opt, board, stats, patterns


def convert2twod(inputlist, length):
    return opt.convert2twod(inputlist, length)

def createboard(size):
    return board.Board(opt.createboard(size))


def initstats(self, history):
    return stats.Stats(history)


def animate(history: list, filename: str, fps=5):
    """Animate a generated history

    ---

    Parameters
    ----------
    history: 3D list 
    - Animates given binary boards, board.history for animating the last simulation of that specific board
    filename: str
    - filename and location for saving the gif

    Retruns
    -------
    saves gif, no return"""
    
    print("animate")

    # if not patternposition:
    #         patternposition = (int(boardsize[0]/2),int(boardsize[1]/2))

    # # Center the pattern
    # patternposition = (patternposition[0]-int(len(pattern[0])/2),
    #                     patternposition[1]-int(len(pattern)/2))

    # # Create board
    # board = sg.Board(size=boardsize)

    # # Add pattern
    # custom_lf = sg.lifeforms.Custom(pattern)
    # board.add(custom_lf, loc=patternposition)

    # # Simulate board
    # sim = sg.Simulator(board)
    # sim.run(sg.rules.conway_classic, iters=iterations)

    # # Create the animation object
    # anim = sim.animate(figsize=boardsize, interval=iterations)

    # # Save the Animation
    # anim.save(f'{filename}.gif', writer='imagemagick', fps=fps)
