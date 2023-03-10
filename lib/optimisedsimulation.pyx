#cython: language_level=3
#cython: boundscheck=False

import copy

cdef int[:] convert2twod(int[:] inputlist, int length):
    cdef int[:,:] twod_list = [[0] * length for _ in range(int(len(inputlist) / length))]
    
    if int(len(inputlist) / length) != len(inputlist) / length:
        raise ValueError("List length must be divisible by length value")
    
    cdef int i, j
    for i in range(int(len(inputlist) / length)):
        for j in range(length):
            twod_list[i][j] = inputlist[length * i + j]

    return twod_list


cdef tuple centerpattern(list[list[int]] pattern, tuple boardsize):
    cdef int x, y
    x = int(boardsize[0] / 2)
    y = int(boardsize[1] / 2)

    x -= int(len(pattern[0]) / 2)
    y -= int(len(pattern) / 2)

    return (x, y)


cdef list[list[int]] createboard(list[list[int]] pattern, tuple boardsize=(100, 100), patternposition=None):
    cdef int i, j
    if patternposition is None:
        patternposition = centerpattern(pattern, boardsize)

    cdef list[list[int]] board = [[0] * boardsize[1] for _ in range(boardsize[0])]

    for i in range(boardsize[0]):
        for j in range(boardsize[1]):
            if i < patternposition[0] or i > patternposition[0] + len(pattern) - 1:
                board[i][j] = 0
            elif j < patternposition[1] or j > patternposition[1] + len(pattern[1]) - 1:
                board[i][j] = 0
            else:
                board[i][j] = pattern[i - patternposition[0]][j - patternposition[1]]

    return board


cdef list[list[int]] run(list[list[int]] board, int iterations, bint fullexport=False):
    cdef list everyboard = []
    cdef int i, g, itrue, ztrue, y, x, sourrounding, surv

    if fullexport:
        everyboard.append(board)

    for g in range(iterations):

        editboard = copy.deepcopy(board)

        for itrue in range(1, len(board) - 1):
            y = itrue
            for ztrue in range(1, len(board[y]) - 1):
                x = ztrue

                places = [board[y - 1][x - 1], board[y - 1][x], board[y - 1][x + 1],
                          board[y][x - 1], board[y][x + 1],
                          board[y + 1][x - 1], board[y + 1][x], board[y + 1][x + 1]]

                sourrounding = sum(places)

                if sourrounding >= 2:
                    surv = checksurvival(sourrounding)
                    if surv == 1:
                        editboard[y][x] = 1
                    elif surv == 2:
                        editboard[y][x] = 0
                else:
                    editboard[y][x] = 0

        board = editboard

        if fullexport:
            everyboard.append(board)
        
    return everyboard if fullexport else board


def checksurvival(sourrounding):
    if sourrounding == 3:
        return 1 # is born
    elif sourrounding == 2:
        return 0 # doesn't change
    elif sourrounding >= 4:
        return 2 # dies
    else:
        return 0 # doesn't change
