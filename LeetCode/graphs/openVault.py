
from collections import deque


def openVault(deadends, target):
    if '0000' in deadends:return -1

    queue = deque()
    queue.append(["0000", 0])
    visited = set(deadends)

    while queue:
        lockSequence, turns = queue.popleft()
        if lockSequence == target:
            return turns

        for child in children(lockSequence):
            if child not in visited:
                queue.append([child, turns + 1])
    
    return -1


def children(lock):
    result = []

    for i in range(4):
        digit = str((int(lock[i]) + 1) % 10)
        result.append(lock[:i] + digit + lock[i+1:])
        digit = str((int(lock[i]) - 1 + 10) % 10)
        result.append(lock[:i] + digit + lock[i+1:])

    return result


deadends = ["0201","0101","0102","1212","2002"]
target = "0202"

print(openVault(deadends, target))
    

    
