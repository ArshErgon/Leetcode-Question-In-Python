class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node = Node(1)
node.next = Node(3)
node.next.next = Node(2)
node.next.next.next = Node(5)
node.next.next.next.next = Node(4)


def sortByMergeSort(node):
    if not node or not node.next:
        return node

    middleNode = findMiddle(node)

    left = sortByMergeSort(node)
    right = sortByMergeSort(middleNode)

    newNode =  merge(left, right)      


    return newNode

def findMiddle(node):
    fast, slow = node.next, node
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    middle = slow.next
    slow.next = None

    return middle



def merge(left, right):
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



print(sortByMergeSort(node))