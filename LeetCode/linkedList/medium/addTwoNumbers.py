from regex import D


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class AddTwoNumbers:

    def addTwoNum(self, node1, node2):
        if not node1 or not node2:
            return node1 or node2

        dummyNode = Node(0)
        tail = dummyNode

        carry = 0

        while node1 is not None or node2 is not None:
            v1 = node1.value if node1 is not None else 0
            v2 = node2.value if node2 is not None else 0
            SUM = v1 + v2 + carry

            tail.next = Node(SUM % 10)
            carry = SUM // 10
            tail = tail.next
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
        
        return dummyNode.next



    def addTwoNumByList(self, node1, node2):
        if not node1 or not node2:
            return node1 or node2

        num1, num2 = [], []

        while node1 is not None:
            num1.append(node1.value)
            node1 = node1.next

        while node2 is not None:
            num2.append(node2.value)
            node2 = node2.next


        num1, num2 = ''.join(map(str, num1[::-1])), ''.join(map(str, num2[::-1]))

        SUM = int(num1) + int(num2)

        num3 = str(SUM)[::-1]

        dummyNode = Node(0)
        tail = dummyNode

        for i in num3:
            tail.next = Node(int(i))
            tail = tail.next

        return dummyNode.next




node1 = Node(2)
node1.next = Node(4)
node1.next.next = Node(3)


node2 = Node(5)
node2.next = Node(6)
node2.next.next = Node(4)

sol = AddTwoNumbers()

print(sol.addTwoNum(node1, node2))

# print(sol.addTwoNumByList(node1, node2))