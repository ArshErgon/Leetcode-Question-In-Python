

# O(n) || O(1)
def uglyNumber(num):

    if num <= 0:
        return False

    for i in [2, 3, 5]:
        while num % i == 0:
            num //= i

    return num == 1

print(uglyNumber(8))
print(uglyNumber(6))