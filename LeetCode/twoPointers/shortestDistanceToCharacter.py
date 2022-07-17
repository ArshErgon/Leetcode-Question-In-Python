

def shortestDistanceToCharacter(string, char):
    sequence = [float('inf')] * len(string)
    newList = []
    for idx, val in enumerate(string):
        if val == char:
            newList.append(idx)

    for val1 in newList:
        for idx2, val2 in enumerate(string):
            sequence[idx2] = min(sequence[idx2], abs(idx2-val1))
    
    return sequence


# print(shortestDistanceToCharacter('loveleetcode', 'e'))



def shortestDistanceToCharacter(string, char):
    n = len(string)
    leftArray, rightArray, result = [float('inf')] * n, [float('inf')] * n, [float('inf')] * n

    temp = float('inf')
    for i in range(len(string)):
        if string[i] == char:
            temp = 0
        leftArray[i] = temp
        temp += 1
    
    temp = float('inf')
    for i in reversed(range(len(string))):
        if string[i] == char:
            temp = 0
        rightArray[i] = temp
        temp += 1


    for i in range(len(result)):
        result[i] = min(leftArray[i], rightArray[i])
    
    return result

    

print(shortestDistanceToCharacter('loveleetcode', 'e'))
