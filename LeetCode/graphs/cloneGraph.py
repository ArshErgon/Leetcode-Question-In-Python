from typing import *

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

hashMap = dict()

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        newCopy = self.makeGraph(node)
        return newCopy
        
    def makeGraph(self, node):
        if node in hashMap:
            return hashMap[node]
        
        copy = Node(node.val)
        hashMap[node] = copy
        
        for neigh in node.neighbors:
            copy.neighbors.append(self.makeGraph(neigh))
            
        return copy


adjList = [[2,4],[1,3],[2,4],[1,3]]
print(Solution().cloneGraph(adjList))