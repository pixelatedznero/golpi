import copy


def convert2twod(inputlist, length):
    twod_list = []
    
    if int(len(inputlist)/length) != len(inputlist)/length:
        raise ValueError("List length must be divisible by length value")
    
    for i in range(int(len(inputlist)/length)):
        twod_list.append(inputlist[length*i:length*i+length])

    return twod_list


def centerpattern(pattern, boardsize):
    patternposition = (int(boardsize[0]/2),int(boardsize[1]/2))

    patternposition = (patternposition[0]-int(len(pattern[0])/2),
                        patternposition[1]-int(len(pattern)/2))
    
    return patternposition


def createboard(size):
    board = []
    
    for h in range(size[1]):
        board.append([])
        for w in range(size[0]):
            board[h].append(0)

    return board


# def createboard(pattern, boardsize=(100,100), patternposition=None):
#     if patternposition == None:
#         patternposition = centerpattern(pattern, boardsize)
# 
#     board = []
# 
#     for i in range(boardsize[0]):
#         board.append([])
#         for j in range(boardsize[1]):
#             if i < patternposition[0] or i > patternposition[0]+len(pattern)-1:
#                 board[i].append(0)
#             elif j < patternposition[1] or j > patternposition[1]+len(pattern[1])-1:
#                 board[i].append(0)
#             else:
#                 board[i].append(pattern[i-patternposition[0]][j-patternposition[1]])
# 
#     return board


def run(board, iterations, fullexport=False):
    if fullexport:
        everyboard = []
        everyboard.append(board)

    for g in range(iterations):
        
        editboard = copy.deepcopy(board)

        for itrue in range(len(board)-2):
            y = itrue+1
            for ztrue in range(len(board[y])-2):
                x = ztrue+1

                places =  [board[y-1][x-1], board[y-1][x], board[y-1][x+1], # up
                            board[y][x-1],                  board[y][x+1],   # middle
                            board[y+1][x-1], board[y+1][x], board[y+1][x+1]] # buttom
                
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