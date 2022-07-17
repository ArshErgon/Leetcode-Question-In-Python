class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class MergeKSortedLists:
    
    def mergeSortedListWithNode(self, listNodes):
        if len(listNodes) == 0 or not listNodes:
            return None

        while len(listNodes) > 1:
            mergeLists = []
            for i in range(0, len(listNodes), 2):
                l1 = listNodes[i]
                l2 = listNodes[i + 1] if (i + 1) < len(listNodes) else None
                
                mergeLists.append(self.mergeTwoLists(l1, l2))
                
            listNodes = mergeLists
            current = listNodes[0]
            while current is not None:
                current = current.next
            
        return listNodes[0]
    
    def mergeTwoLists(self, list1, list2):
        newDummyNode = Node(0)
        tail = newDummyNode

        while list1 is not None and list2 is not None:
            if list1.value < list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail = list1 or list2

        return newDummyNode.next


node1 = Node(1)
node1.next = Node(4)
node1.next.next = Node(5)

node2 = Node(1)
node2.next = Node(3)
node2.next.next = Node(4)

node3 = Node(2)
node3.next = Node(6)

node4 = Node(4)
node4.next  = Node(8)

sol = MergeKSortedLists()
x = (sol.mergeSortedListWithNode([node1, node2, node3, node4]))
while x is not None:
    print(x.value, end='-->')
    x = x.next
