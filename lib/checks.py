class Checks:
    
    def __init__(self, everyboard):
        self.everyboard = everyboard


    def distance(self):
        lastboard = self.everyboard[len(self.everyboard)-1]
        distances = {"up":0, "down":0, "right":0, "left":0}

        for i in range(len(lastboard)):
            if sum(lastboard[i]) > 0:
                distances["up"] = int(len(lastboard)/2) - i
                break
        
        for i in reversed(range(len(lastboard))):
            if sum(lastboard[i]) > 0:
                distances["down"] = i - int(len(lastboard)/2)
                break
        
        for x in range(len(lastboard)):
            for i in range(len(lastboard[x])):
                if lastboard[x][i] > 0:
                    distances["left"] = int(len(lastboard[x])/2) - i
                    break
            if distances["left"] > 0:
                break
        
        for x in range(len(lastboard)):
            for i in reversed(range(len(lastboard[x]))):
                if lastboard[x][i] > 0:
                    distances["right"] = i - int(len(lastboard[x])/2)
                    break
            if distances["right"] > 0:
                break

        for i in distances:
            if distances[i] < 0:
                distances[i] = 0

        return distances
                

    def pixelsperframe(self):
        print(f"pxl{self.everyboard}")