class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next



class InsertationSort:


    # Worse: O(n^2)
    # bes O(N)
    def insertationSort(self, node):
        if not node or node.next is None:
            return node
        
        dummyNode = Node(0, node)
        prev, current = node, node.next


        while current is not None:
            if current.value >= prev.value:
                prev, current = current, current.next
                continue
        
            tmp = dummyNode

            while current.value > tmp.next.value:
                tmp = tmp.next

            prev.next = current.next
            current.next = tmp.next
            tmp.next = current
            current = prev.next



        x = dummyNode.next

        while x is not None:
            print(x.value, end='--->')
            x = x.next




    # O(n^2) || O(n)
    def insertationSortByList(self, node):
        if not node or not node.next:
            return node

        stack = []

        while node is not None:
            stack.append(node.value)
            node = node.next

        sortedList =  self.insertationSortForList(stack)
        dummyNode = Node(0)
        tail = dummyNode

        for i in sortedList:
            tail.next = Node(i)
            tail = tail.next

        return dummyNode.next


    def insertationSortForList(self, stack):
        if not stack:
            return

        newList = [stack[0]]
        for val in stack[1:]:
            i = 0
            while i <= len(newList)-1 and val > newList[i]:
                i += 1
            
            newList.insert(i, val)

        return newList
                



node = Node(4)
node.next = Node(2)
node.next.next = Node(1)
node.next.next.next = Node(3)


sol = InsertationSort()

print(sol.insertationSort(node))
# print(sol.insertationSortByList(node))