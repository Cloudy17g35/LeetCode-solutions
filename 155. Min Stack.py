class MinStack:

    def __init__(self):
        self.container = []
        self.min_container = []
        

    def push(self, val: int) -> None:
        self.container.append(val)
        val = min(val, self.min_container[-1] if self.min_container else val)
        self.min_container.append(val)
        
    def pop(self) -> None:
        self.container.pop()
        self.min_container.pop()

    def top(self) -> int:
        return self.container[-1]
        

    def getMin(self) -> int:
        return self.min_container[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
