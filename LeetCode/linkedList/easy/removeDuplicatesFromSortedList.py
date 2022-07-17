

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class RemoveDuplicateNode:
    def removeDuplicates(self, node):
        if not node:
            return node
        prev, nextNode = node, node.next
        while nextNode:
            if prev.value == nextNode.value:
                prev.next = nextNode.next
                nextNode = nextNode.next
            else:
                prev = nextNode
                nextNode = nextNode.next
                
        return node


node = Node(1)
node.next = Node(1)
node.next.next = Node(2)
node.next.next.next = Node(3)
node.next.next.next.next = Node(3)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(4)

sol = RemoveDuplicateNode()

print(sol.removeDuplicates(node))
