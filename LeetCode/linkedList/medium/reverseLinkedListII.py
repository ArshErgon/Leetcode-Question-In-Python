class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None




class ReverseLinkedList:

    def reverseList(self, node, left, right):
        if not node or left == right:
            return node

        dummyNode = Node(0)
        dummyNode.next = node
        prevLeft, current = dummyNode, node

        for i in range(left - 1):
            prevLeft = current
            current = current.next

        prev = None

        for i in range(right - left + 1):
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        prevLeft.next.next = current
        prevLeft.next = prev

        x = dummyNode.next

        while x is not None:
            print(x.value, end='-->')
            x = x.next
        
            


    # O(N) || O(n)
    def reverseListByList(self, node, left, right):
        if not node or left == right:
            return node

        stack = []
        dummyNode = Node(0)
        tail = dummyNode

        while node is not None:
            stack.append(node.value)
            node = node.next

        newStack = stack[:left-1] + stack[left-1:right][::-1] + stack[right:]

        for i in newStack:
            tail.next = Node(i)
            tail = tail.next

        return dummyNode.next





node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)


sol = ReverseLinkedList()

print(sol.reverseList(node, 2, 4))
# print(sol.reverseListByList(node, 2, 4))