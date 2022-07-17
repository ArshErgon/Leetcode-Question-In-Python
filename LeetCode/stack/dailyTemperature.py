



def dailyTemperatures(temperatures):
    waitingList = [0] * len(temperatures)
    stack = []
    
    for idx, val in enumerate(temperatures):
        while len(stack) > 0 and temperatures[stack[len(stack) - 1]] < val:
            current = stack.pop()
            waitingList[current] = idx - current
            
        stack.append(idx)
        
    return waitingList