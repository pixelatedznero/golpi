class Simulation:

    def __init__(self):
        board = []
        oneline = []
        for i in range(60*2+15):
            oneline.append(0)
        for i in range(60*2+15):
            board.append(oneline)

        self.emptyboard = board


    def convert2twod(self, inputlist, length):
        twod_list = []
        
        if int(len(inputlist)/length) != len(inputlist)/length:
            raise ValueError("List length must be divisible by length value")
        
        for i in range(int(len(inputlist)/length)):
            twod_list.append(inputlist[length*i:length*i+length])

        return twod_list

    def run(self, inputpattern, boardsize=(100,100), patternposition=None):
        if patternposition == None:
            patternposition = (int(boardsize[0]/2), int(boardsize[1]/2))
        patternposition = (patternposition[0]-int(len(inputpattern)/2), patternposition[1]-int(len(inputpattern[0])/2))
        board = []
        for i in range(boardsize[0]):
            board.append([])
            for j in range(boardsize[1]):
                if i < patternposition[0] or i > patternposition[0]+len(inputpattern)-1:
                    board[i].append(0)
                elif j < patternposition[1] or j > patternposition[1]+len(inputpattern[1])-1:
                    board[i].append(0)
                else:
                    board[i].append(inputpattern[i-patternposition[0]][j-patternposition[1]])

        for g in range(2):
            
            print(board[43][43:49])
            print(board[44][43:49])
            print(board[45][43:49])
            print(board[46][43:49])
            print(board[47][43:49])
            print(board[48][43:49])
            print("------")

            editboard = board

            for itrue in range(len(board)-2):
                i = itrue+1
                for ztrue in range(len(board[i])-2):
                    z = ztrue+1

                    upper = [board[i-1][z-1], board[i-1][z], board[i-1][z+1]]
                    middle = [board[i][z-1], board[i][z+1]]
                    lower = [board[i+1][z-1], board[i+1][z], board[i+1][z+1]]

                    # upper = [board[i-1][z-1] if z-1>=0 else 0, board[i-1][z], board[i-1][z+1] if z+1<135 else 0] if i-1>=0 else [0,0,0]
                    # middle = [board[i][z-1] if z-1>=0 else 0, board[i][z+1] if z+1<135 else 0]
                    # lower = [board[i+1][z-1] if z-1>=0 else 0, board[i+1][z], board[i+1][z+1] if z+1<135 else 0] if i+1<135 else [0,0,0]
                    
                    sourrounding = 0
                    for f in upper:
                        sourrounding += f
                    for f in middle:
                        sourrounding += f
                    for f in lower:
                        sourrounding += f

                    if sourrounding >= 2:
                        surv = self.checksurvival(sourrounding)
                        if surv == 1:
                            editboard[i][z] = 1
                        elif surv == 2:
                            editboard[i][z] = 0
                    else:
                        editboard[i][z] = 0

            board = editboard



    def checksurvival(self, sourrounding):
        if sourrounding == 3:
            return 1 # is born
        elif sourrounding == 2:
            return 0 # doesn't change
        elif sourrounding >= 4:
            return 2 # dies
        else:
            return 0 # doesn't change



gm = Simulation()

gm.run(gm.convert2twod([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                        0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,
                        0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,
                        0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,
                        0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,
                        0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,
                        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       15)
       )

print("dada")
