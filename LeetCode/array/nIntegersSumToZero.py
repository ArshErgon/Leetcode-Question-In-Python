

def nIntegersSumUpToZero(n):
    if n == 1:
        return 0
    return list(range(1-n, n, 2))


print(nIntegersSumUpToZero(5))