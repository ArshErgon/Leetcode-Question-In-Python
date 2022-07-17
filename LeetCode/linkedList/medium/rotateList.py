

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class RotateList:

    def rotateList(self, node, k):
        if not node or k == 0:
            return node
        k = self.findLength(node, k)
        if k == 0:
            return node

        slow, fast = node, node
        for _ in range(k):
            fast = fast.next

        while fast is not None and fast.next is not None:
            fast = fast.next
            slow = slow.next

        secondHalf = slow.next
        print(secondHalf.value)
        slow.next = None
        fast.next = node
        node = secondHalf

        while node is not None:
            print(node.value, end='--->')
            node = node.next
    
    def findLength(self, node, k):
        length = 0
        while node is not None:
            length += 1
            node = node.next

        return (k % length)



node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)

sol = RotateList()
print(sol.rotateList(node, 2))