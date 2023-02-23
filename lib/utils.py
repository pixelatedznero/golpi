import seagull as sg

try:
    from lib import checks
except:
    import checks

class Utils:
    
    def __init__(self):
        print("utilself")
        self.checks = checks

    def animategif(self, pattern=list, iterations=int, filename=str, fps=5, boardsize=(100,100), patternposition=None):
        if not patternposition:
            patternposition = (int(boardsize[0]/2),int(boardsize[1]/2))

        print(patternposition)

        # Center the pattern
        patternposition = (patternposition[0]-int(len(pattern[0])/2),
                           patternposition[1]-int(len(pattern)/2))
        
        print(patternposition)

        # Create board
        board = sg.Board(size=boardsize)

        # Add pattern
        custom_lf = sg.lifeforms.Custom(pattern)
        board.add(custom_lf, loc=patternposition)

        # Simulate board
        sim = sg.Simulator(board)
        sim.run(sg.rules.conway_classic, iters=iterations)

        # Create the animation object
        anim = sim.animate(figsize=boardsize, interval=iterations)

        # Save the Animation
        anim.save(f'{filename}.gif', writer='imagemagick', fps=fps)
