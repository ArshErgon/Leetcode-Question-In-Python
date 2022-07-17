

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class MergeTwoSortedList:


# O(N + M) || O(n)
    def mergeListByDummy(self, node1, node2):
        if not node1 or not node2:
            return node1 or node2

        dummyNode = Node(0)
        tail = dummyNode

        while node1 is not None and node2 is not None:
            if node1.value < node2.value:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            tail = tail.next

        tail.next = node1 or node2

        return dummyNode.next

# O(N+M) || O(N)
# worse O(N^2)
    def mergeListsByList(self, node1, node2):
        if not node1 or not node2:
            return node1 or node2

        
        stack = []

        while node1 is not None:
            stack.append(node1.value)
            node1 = node1.next

        
        while node2 is not None:
            i = 0
            while len(stack) > i and node2.value > stack[i]:
                i += 1

            stack.insert(i, node2.value)

            node2 = node2.next

        dummyNode = Node(0)
        tail = dummyNode
        while stack:
            tail.next = Node(stack.pop(0))
            tail = tail.next

        return dummyNode.next



node1 = Node(1)
node1.next = Node(2)
node1.next.next = Node(4)

node2 = Node(1)
node2.next = Node(3)
node2.next.next = Node(4)

sol = MergeTwoSortedList()

print(sol.mergeListByDummy(node1, node2))
print(sol.mergeListsByList(node1, node2))