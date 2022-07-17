

from heapq import heapify, heappop, heappush

class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k 
        self.heap = nums
        heapify(self.heap)
        while len(self.heap) > k:
            heappop(self.heap)


    def add(self, val):
        heappush(self.heap, val)
        return self.getKthLargest()

    def getKthLargest(self):
        if self.k < len(self.heap):
            heappop(self.heap)

        return self.heap[0]



sol = KthLargest(3, [4, 5, 8, 2])
print(sol.add(3))
print(sol.add(5))
print(sol.add(10))
print(sol.add(9))
print(sol.add(4))

print(sol.printList())