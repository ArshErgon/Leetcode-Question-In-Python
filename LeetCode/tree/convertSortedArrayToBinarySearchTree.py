class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None





def aHeightBST(array):
    if not array:
        return 

    mid = len(array) // 2
    root = Node(array[mid])
    root.left = array[:mid]
    root.right = array[mid + 1:]


    return root

    