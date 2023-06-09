def convert_to_2d(input_list: list, x_length: int) -> list:
    """ Converts a 1D list into a 2D list with provided x-length

    Parameters
    ----------
    input_list: list
    - 1D list that must be converted to 2D list

    x_length: int
    - The row length that the new 2d list will have

    Returns
    -------
    The provied 1D list converted into a 2D list with given row length """

    if len(input_list) % x_length != 0:
        raise Exception("List must be divisible by x_length in order to be converted to 2d list.")
    
    return [[input_list[y * x_length + x] for x in range(0, x_length)] for y in range(0, len(input_list) // x_length)]

def convert_to_binary(input_list: list) -> list:
    """ Converts a list of space-star representation into a list of binary representation

    Parameters
    ----------
    input_list: list
    - 1D list that will be converted to binary represenation

    Returns
    -------
    The provided 1D list of space-star representation as a binary representation """

    return [1 if (i == 42 or i == '*') else 0 for i in input_list]

def convert_binary_to_2d(input_binary: bytes, x_length: int, alive: bytes = b'*') -> list:
    """ Converts a binary list into a 2D list with provided x-length

    Parameters
    ----------
    input_binary: bytes
    - bytes object to be converted

    x_length: int
    - The row length that the new 2d list will have

    alive: bytes (optional)
    - the charakter that should be converted into a 1 for alive cell, all others will be turned to 0 for dead cell

    Returns
    -------
    The provied bytes object converted into a 2D list with given row length and integers 1 and 0 for alive and dead"""

    if len(input_binary) % x_length != 0:
        raise Exception("List must be divisible by x_length in order to be converted to 2d list.")
    
    converted = convert_to_2d(input_binary, x_length)

    for ikey, i in enumerate(converted):
        for jkey, j in enumerate(i):

            if i[jkey] == int.from_bytes(alive, byteorder='big'):
                converted[ikey][jkey] = 1
            else:
                converted[ikey][jkey] = 0

    return converted


#def animate(history: list, filename: str, fps=5):
"""Animate a generated history

Parameters
----------
history: 3D list 
- Animates given binary boards, board.history for animating the last simulation of that specific board

filename: str
- filename and location for saving the gif

Retruns
-------
saves gif, no return"""
    
#    print("animate")

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
