


def uniqueBinaryTree(n):
    
    treeNode = [1] * (n + 1)

    for nodes in range(2, n + 1):
        total = 0
        for i in range(1, nodes + 1):
            left = i-1
            right = nodes - i
            # treeNode[nodes] += treeNode[i - 1] * treeNode[nodes - i]
            total += treeNode[left] * treeNode[right]
        treeNode[nodes] = total
    
    return treeNode[n]


print(uniqueBinaryTree(3))

        