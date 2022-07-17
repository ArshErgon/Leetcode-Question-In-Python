

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class ReverseLinkedList:
# O(n) || O(1)
    def reverseIterator(self, node):
        if not node:
            return node

        prev = None
        newNode = node
        while newNode is not None:
            next = newNode.next
            newNode.next = prev
            prev = newNode
            newNode = next
        
        while prev is not None:
            print(prev.value, end='--->')
            prev = prev.next


    # O(N) || O(N)
    def reverseRecursive(self, node):
        if not node:
            return node

        if node.next is None:
            return node

        newNode = self.reverseRecursive(node.next)
        node.next.next = node
        node.next = None
        return newNode

    # O(N) || O(N)

    def reverseWithStack(self, node):
        if not node:
            return node

        stack = []

        newNode = node
        while newNode is not None:
            stack.append(newNode)
            newNode = newNode.next

        newNode = node

        while stack:
            newNode.next = stack.pop()
            newNode = newNode.next

        return node


node = Node(5)
node.next = Node(4)
node.next.next = Node(3)
node.next.next.next = Node(2)
node.next.next.next.next = Node(1)


sol = ReverseLinkedList()

print(sol.reverseIterator(node))
print(sol.reverseWithStack(node))
