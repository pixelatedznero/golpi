#from .golpi import convert_to_2d, convert_to_binary

class Stats:
    def __init__(self, history: bytes, latest_history: bytes) -> None:
        self.history = convert_to_2d(convert_to_binary(list(history)))
        self.latest_history = convert_to_2d(convert_to_binary(list(latest_history)))

    def distance(self):
        """ Computes the distance that every pixel has traveled in every direction

        Parameters
        ----------
        None

        Returns
        -------
        Dictionary of the distances in every direction (up, down, right and left) """

        distances = { "up" : 0, "down" : 0, "right" : 0, "left" : 0 }

        """
        for i in range(len(self.latest_history)):
            if sum(self.latest_history[i]) > 0:
                distances["up"] = len(self.latest_history) // 2 - i
                break
        
        for i in reversed(range(len(self.latest_history))):
            if sum(self.latest_history[i]) > 0:
                distances["down"] = i - len(self.latest_history) // 2
                break
        
        for x in range(len(self.latest_history)):
            for i in range(len(self.latest_history[x])):
                if self.latest_history[x][i] > 0:
                    distances["left"] = len(self.latest_history[x]) // 2 - i
                    break
            if distances["left"] > 0:
                break
        
        for x in range(len(self.latest_history)):
            for i in reversed(range(len(self.latest_history[x]))):
                if self.latest_history[x][i] > 0:
                    distances["right"] = i - len(self.latest_history[x]) // 2
                    break
            if distances["right"] > 0:
                break

        for i in distances:
            if distances[i] < 0:
                distances[i] = 0

        return distances
        """

        

    def pixels_per_frame(self):
        """ Computes the average of alive pixels for all frames

        Parameters
        ----------
        None

        Returns
        -------
        Average of alive pixels for all frames """

        total_pixels = 0
        for i in range(len(self.history)):
            for j in range(len(self.history[i])):
                total_pixels += sum(self.history[i][j])
                
        return total_pixels / len(self.history)

    def survived_time(self):
        """ The amount of frames until all cells were dead

        Parameters
        ----------
        None

        Returns
        -------
        Frames until the board was dead """

        frames = 0
        for i in range(len(self.history)): # one frame
            pixels = 0
            for j in range(len(self.history[i])): # one row
                pixels += sum(self.history[i][j])
            
            if pixels > 0: 
                frames += 1
            else:
                break
        return frames
