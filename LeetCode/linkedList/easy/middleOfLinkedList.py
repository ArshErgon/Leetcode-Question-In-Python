class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)
node.next.next.next.next.next = Node(6)
node.next.next.next.next.next.next = Node(7)
node.next.next.next.next.next.next.next = Node(8)
node.next.next.next.next.next.next.next.next = Node(9)
node.next.next.next.next.next.next.next.next.next = Node(10)




def middleOfLinkedList(node):
    if not node:
        return None
    fast, slow = node, node

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    
    return slow
    


print(middleOfLinkedList(node))
    