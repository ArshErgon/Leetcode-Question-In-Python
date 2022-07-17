
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)

node2 = Node(6)
node2.next = Node(7)
node2.next.next = Node(8)
node2.next.next.next = Node(9)
node2.next.next.next.next = Node(10)


def mergeTwoSortedLinkedListByDummyNode(node1, node2):
    if not node1 or not node2:
        return node1 or node2

    dummyNode = Node(0)

    while node1 is not None and node2 is not None:
        if node1.value < node2.value:
            dummyNode.next = node1
            node1 = node1.next
        else:
            dummyNode.next = node2
            node2 = node2.next
        
        dummyNode = dummyNode.next
    
    dummyNode.next = node1 or node2

    return dummyNode.next

# O(N) || O(N)
def mergeTwoSortedLinkedListByList(node1, node2):
    if not node1 or not node2:
        return node1 or node2

    sortedList = []

    while node1 is not None:
        sortedList.append(node1.value)
        node1 = node1.next

    
    i = 0
    while node2 is not None:
        while i < len(sortedList) and sortedList[i] < node2.value:
            i += 1
        sortedList.insert(i, node2.value)
        i = 0
        node2 = node2.next

    dummyNode = Node(0)

    for i in sortedList:
        dummyNode.next = Node(i)
        dummyNode = dummyNode.next
    
    return dummyNode.next
        

print(mergeTwoSortedLinkedListByList(node, node2))