

def canPlaceFlower(f, n):
    for i in range(len(f)):
        leftOk = i == 0 or f[i-1] == 0
        rightOk = i == len(f) -1 or f[i+1] == 0
        if leftOk and f[i] == 0 and rightOk:
            f[i] = 1
            n -= 1
    return n <= 0


l = [1,0,0,0,0,1]
i = 2

print(canPlaceFlower(l, i))


def canPlaceFlower(array, n):
    if not array:
        return False

    if len(array) == 1:
        return array[0] == 0
    
    if len(array) == 2:
        return array[0] == 0 and array[1] == 0

    seen = [True] * len(array)

    for i in range(len(array) - 1):
        if array[i] == 1 and array[i+1] == 0:
            seen[i+1], seen[i] = None, False

        elif array[i] == 0 and array[i+1] == 1:
            seen[i], seen[i+1] = None, False

    
    print(seen)


    for i in range(1, len(seen) - 1):
        if seen[i] and seen[i-1] == None:
            seen[i] = False
            seen[i+1] = False
            n -= 1
        
        if seen[i+1] and seen[i] == None:
            seen[i+1] = False
            seen[i] = False
            n -= 1

    for i in range(len(array) - 1):
        if seen[i] and seen[i + 1] == None:
            seen[i] = False
            seen[i+1] = False
            n -= 1

    


    return seen



l = [1,0,0,0,0,1]
i = 2


2

# print(canPlaceFlower(l, i))