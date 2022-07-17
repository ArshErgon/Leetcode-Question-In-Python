class Node:
    def __init__(self, value):
        self.value = value
        self.next = None




class MergeSortedList:
    
    def mergeSortedListWithArray(self, node1, node2):
        if not node1 or not node2:
            return node1 or node2

        dummyNode = Node(0)
        tail = dummyNode

        while node1 is not None and node2 is not None:
            if node1.value < node2.value:
                tail.next = Node(node1.value)
                node1 = node1.next
            else:
                tail.next = Node(node2.value)
                node2 = node2.next
            
            tail = tail.next

        tail.next = node1 or node2
       
        while dummyNode is not None:
            print(dummyNode.value, end='-->')
            dummyNode = dummyNode.next



node1 = Node(1)
node1.next = Node(2)
node1.next.next = Node(4)

node2 = Node(1)
node2.next = Node(3)
node2.next.next = Node(4)

sol = MergeSortedList()

print(sol.mergeSortedListWithArray(node1, node2))