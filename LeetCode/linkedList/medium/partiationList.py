class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class PartiationList:
    def partiation(self, node, x):
        if not node:
            return node

        tmp = ans = Node(0)
        tmp1 = prev = Node(0)

        while node is not None:
            if node.value < x:
                tmp.next = node
                tmp = tmp.next
            else:
                prev.next = node
                prev = prev.next

            node = node.next

        prev.next = None

        tmp.next = tmp1.next

        x = ans.next
        while x is not None:
            print(x.value, end='--->')
            x = x.next

    def partiationByList(self, node, x):
        if not node:
            return node

        l1, l2 = [], []
        newNode = node
        while newNode is not None:
            if newNode.value < x:
                l1.append(newNode.value)
            else:
                l2.append(newNode.value)
            newNode = newNode.next

        combineList = l1 + l2
        dummyNode = Node(0)
        tail = dummyNode

        for i in combineList:
            tail.next = Node(i)
            tail = tail.next

        return dummyNode.next

        
node = Node(1)
node.next = Node(4)
node.next.next = Node(3)
node.next.next.next = Node(2)
node.next.next.next.next = Node(5)
node.next.next.next.next.next = Node(2)

sol = PartiationList()

print(sol.partiation(node, 3))
# print(sol.partiationByList(node, 3))