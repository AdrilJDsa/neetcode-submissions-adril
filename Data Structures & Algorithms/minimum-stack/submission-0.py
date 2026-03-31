class MinStack:

    def __init__(self):
        self.length = 0
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length += 1
        return None


    def pop(self) -> None:
        if self.length == 0:
            return None
        self.stack.pop(self.length-1)
        self.length -= 1
        return None

        
    def top(self) -> int:
        if self.length == 0:
            return 0
        return self.stack[self.length - 1]
        

    def getMin(self) -> int:
        return min(self.stack)
        
