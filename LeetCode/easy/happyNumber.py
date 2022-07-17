
# O(n) || O(n)
def happyNumber(n):

    while n not in [1, 4]:
        n = splitNumberHelper(n)

    return n == 1


def splitNumberHelper(number):
    square = 0
    while number > 0:
        square += pow(number % 10, 2)
        number //= 10

    return square


print(happyNumber(19))