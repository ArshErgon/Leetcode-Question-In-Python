
def countOneBits(n):
    n = int(bin(n)[2:])
    count = 0
    while n > 0:
        isOne = n % 10 == 1
        if isOne:
            count += 1
        n //= 10

    return count

# print(countOneBits(11))
# print(countOneBits(4294967293))


def countOneBits(n):
    return bin(n)[2:].count('1')

# print(countOneBits(11))


def countOneBits(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

print(countOneBits(11))


def countOneBits(n):
    count = 0
    while n > 0:
        count += 1 if n % 2 == 1 else 0
        n //= 2

    return count

# print(countOneBits(11))
