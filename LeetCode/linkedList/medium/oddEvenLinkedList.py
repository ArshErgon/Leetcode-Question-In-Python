

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None

node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)


def oddEvenLinkedList(node):
    if not node:
        return []

    odd = node
    even = node.next
    evenHead = even
    while odd and even and odd.next and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = evenHead

    return node

print(oddEvenLinkedList(node))