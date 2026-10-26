class MinStack:

    def __init__(self):
        self.m = []
        self.arr = []

    def push(self, val: int):
        self.arr.append(val)
        val = min(val, self.m[-1] if self.m else val)
        self.m.append(val)

    def pop(self):
        self.arr.pop()
        self.m.pop()
       
    def top(self):
        return self.arr[-1]
        

    def getMin(self):
        print(self.m)
        return self.m[-1]
        
