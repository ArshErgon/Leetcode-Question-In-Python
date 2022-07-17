




class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        newVal = {'min':val}
        if len(self.minStack) > 0:
            newVal['min'] = min(self.minStack[-1]['min'], val)
        
        self.stack.append(val)
        self.minStack.append(newVal)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        return self.minStack[len(self.stack)-1]['min']