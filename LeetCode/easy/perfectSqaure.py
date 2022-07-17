

# O(n) || O(1)

def perfectSquare(n):
    if not n:
        return False
    
    for i in range(1, n + 1):
        square = (i * i)

        if square == n:
            return True

        elif square > n:
            return False

    return -1

# print(perfectSquare(16))

# O(logN) || O(1)
def perfectSquare(n):
    if not n:
        return False

    left, right = 0, n + 1

    while left <= right:
        mid = (left + right) // 2

        square = mid ** 2

        if square == n:
            return True

        elif square > n:
            right = mid - 1

        else:
            left = mid + 1

    return False

print(perfectSquare(16))