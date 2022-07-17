
from heapq import heapify, heappush, heappop

def handOfStraight(hand, group):
    if not hand:
        return group == 0
    
    if len(hand) % group != 0:return False

    hashMap = dict()
    for i in hand:
        hashMap[i] = 1 + hashMap.get(i, 0)
    
    keys = list(hashMap.keys())
    heapify(keys)

    while keys:
        first = keys[0]

        for i in range(first, first + group):
            if i not in hashMap:
                return False

            hashMap[i] -= 1
            if hashMap[i] == 0:
                if i != keys[0]:
                    return False
                heappop(keys)

    
    return True

    
print(handOfStraight([1,2,3,6,2,3,4,7,8], 3))
print(handOfStraight([1,2,3,4,5], 4))
