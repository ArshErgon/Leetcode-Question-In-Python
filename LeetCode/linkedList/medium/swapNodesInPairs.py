class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

    

class SwapNodesInPairs:

    def swapPairs(self, head):
        dummyNode = Node(0, head)
        prev, current = dummyNode, head
        while current and current.next:
            nextPair = current.next.next
            second = current.next

            second.next = current
            current.next = nextPair
            prev.next = second

            prev = current
            current = nextPair

        return dummyNode.next


