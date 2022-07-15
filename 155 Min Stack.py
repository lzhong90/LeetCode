class MinStack:

    def __init__(self):
        self.stck = []
        self.min = []

    def push(self, val: int) -> None:
        self.stck.append(val)
        if len(self.min) > 0:
            if val <= self.min[-1]:
                self.min.append(val)
        else:
            self.min.append(val)
        
        

    def pop(self) -> None:
        val = self.stck.pop()
        if len(self.min) > 0 and val == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stck[-1]

        

    def getMin(self) -> int:
        return self.min[-1]
