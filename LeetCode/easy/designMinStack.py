class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        newMinStack = {'min':val}
        if len(self.minStack) > 0:
            newMinStack['min'] = min(self.minStack[-1]['min'], val)
        
        self.minStack.append(newMinStack)
        self.stack.append(val)
        
    def pop(self):
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[len(self.stack)-1]
        

    def getMin(self):
        return self.minStack[len(self.minStack)-1]['min']