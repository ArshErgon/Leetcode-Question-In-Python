


def permutation(n, k):
    if not n:
        return n
    
    n = list(range(1, n+1))
    
    hashMap = list()

    count = 1
    permutate(n, hashMap, 0)
    return ''.join(str(x) for x in hashMap[k]), hashMap

def permutate(n, hashMap, i):
 

    if i == len(n) - 1:
        hashMap.append(n[:])

    else:
        for x in range(i, len(n)):
            swap(n, i, x)
            permutate(n, hashMap, i + 1)
            swap(n, i, x)


def swap(n, i, j):
    n[i], n[j] = n[j], n[i]


print(permutation(3, 3))