



# O(nlogn) || O(1) or say O(n) because some sorting takes stack memory;
def lastStoneWeight(stones):
    while len(stones) > 1:
        stones.sort()
        a = stones.pop()
        b = stones.pop()
        if a != b:
            stones.append(a - b)
    return stones[0] if stones else 0


print(lastStoneWeight([2,7,4,1,8,1]))


from heapq import heapify, heappop, heappush

def lastStoneWeight(stones):
    if len(stones) == 1:
        return stones[0]
    stones = [-x for x in stones]
    heapify(stones)

    while len(stones) > 1:
        x, y = heappop(stones), heappop(stones)

        if x == y:
            continue

        else:
            heappush(stones, x - y)

    return stones[0]  * -1 if len(stones) == 1 else 0


print(lastStoneWeight([2,7,4,1,8,1]))