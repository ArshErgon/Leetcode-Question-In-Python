class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node = Node(2)
node.next = Node(7)
node.next.next = Node(4)
node.next.next.next = Node(3)
node.next.next.next.next = Node(5)
[1,7,5,1,9,2,5,1]
[7, 9, 9, 9, 0, 5, 0, 0]

def nextLargerNode(head):
    if not head:
        return [0]
    result, stack = [], []
    while head is not None:
        while stack and stack[-1][1] < head.value:
            result[stack.pop()[0]] = head.value
        stack.append([len(result), head.value])
        result.append(0)
        head = head.next
    return result

print(nextLargerNode(node))