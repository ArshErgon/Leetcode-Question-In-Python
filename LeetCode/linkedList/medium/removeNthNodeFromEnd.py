
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None



class RemoveNthNodeFromEnd:
    # O(n) with O(1)
    def removeNthNodeDummy(self, node, n):
        if not node:
            return node

        slow, fast = node, node

        for _ in range(n):
            fast = fast.next

        if not fast:return node

        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
               
        slow.next = slow.next.next

        while node is not None:
            print(node.value, end='--->')
            node = node.next

    # O(n) || O(N)
    def removeNthNodeByStack(self, node, n):
        if not node:
            return node

        stack = []

        while node is not None:
            stack.append(node.value)
            node = node.next

        stack.pop(-n)

        dummyNode = Node(0)
        tail = dummyNode

        for i in stack:
            tail.next = Node(i)
            tail = tail.next
        
        return dummyNode.next



node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)
node.next.next.next.next.next = Node(6)


sol = RemoveNthNodeFromEnd()
print(sol.removeNthNodeDummy(node, 2))