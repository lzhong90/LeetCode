from collections import deque
class MovingAverage:
    def __init__(self, k):
        self.length=k
        self.window=deque()
        self.res=0
    def next(self, input):
        
        self.add(input)
        
        
        return self.res/len(self.window)
    
    def add(self, input):
        if len(self.window) < self.length:
            self.window.append(input)
            self.res += input
        else:
            self.res -= self.window.popleft()
            self.window.append(input)
            self.res += input
