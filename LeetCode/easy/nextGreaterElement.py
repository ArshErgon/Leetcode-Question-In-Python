

# O(n*m) || O(n+m)
def nextGreaterElement(num1, num2):
    result = list()
    for i in num1:
        isCross = False
        isChange = False
        for j in num2:
            if j == i:
                isCross = True
            
            if isCross and i < j:
                result.append(j)
                isChange = True
                break
        
        if not isChange:
            result.append(-1)
        

    return result


# print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))



def nextGreaterElementWithMonotonic(num1, num2):
    monotonicArray = []
    stack = [-1] * len(num1)
    indexMap = {v:i for i,v in enumerate(num1)}
    for i in num2:
        while len(monotonicArray) > 0 and monotonicArray[-1] < i:
            elementPop = monotonicArray.pop()
            if elementPop in indexMap:
                stack[indexMap[elementPop]] = i
        monotonicArray.append(i)
    return stack

print(nextGreaterElementWithMonotonic([4, 1, 2], [1, 3, 4, 2]))
