



from heapq import heappush, heappop
from collections import defaultdict


# O(E*logV)
# e is edges, log for minheap, v for vertices

def networkDelayTime(times, n, k):
    
    edges = defaultdict(list)

    for ui, vi, wi in times:
        edges[ui].append((vi, wi))

    minHeap = [(0, k)]
    times = 0
    visited = set()
    while minHeap:
        weight, node = heappop(minHeap)

        if node in visited:
            continue

        visited.add(node)
        times = max(times, weight)

        for node2, weight2 in edges[node]:
            if node2 not in visited:
                heappush(minHeap, (weight + weight2, node2))


    return times if len(visited) == n else -1


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

print(networkDelayTime(times, n, k))
            

