class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = None



class SortList:

    def sortByMergeSort(self, node):
        if not node or not node.next:
            return node

        middleNode = self.findMiddle(node)

        left = self.sortByMergeSort(node)
        right = self.sortByMergeSort(middleNode)

        newNode =  self.merge(left, right)      


        while newNode is not None:
            print(newNode.value, end='--->')
            newNode = newNode.next

    def findMiddle(self, node):
        fast, slow = node.next, node
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None
    
        return middle


    
    def merge(self, left, right):
        if not left or not right:
            return left or right

        dummyNode = p = Node(0)  

        while left is not None and right is not None:
            if left.value < right.value:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next

        
        p.next = left or right

        return dummyNode.next






    def SortListByList(self, node):
        if not node or not node.next:
            return node

        stack = []

        newNode = node
        while newNode is not None:
            stack.append(newNode.value)
            newNode = newNode.next


        stack.sort()
        realNodeInsert = node
        for i in stack:
            realNodeInsert.value = i
            realNodeInsert = realNodeInsert.next

        while node is not None:
            print(node.value, end="--->")
            node = node.next

        


node = Node(1)
node.next = Node(3)
node.next.next = Node(2)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)
# node.next.next.next.next.next = Node(0)


sol = SortList()

print(sol.sortByMergeSort(node))
# print(sol.SortListByList(node))