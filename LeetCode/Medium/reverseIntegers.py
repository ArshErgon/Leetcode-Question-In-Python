



# O(n) || O(n*m)
def reverseIntegerByString(value):
    isNeg = value < 0
    strVal = str(abs(value))
    strVal = int(strVal[::-1])
    return -strVal if isNeg else strVal


# O(n) || O(1)
def reverseIntegerByList(value):
    if value == 0:return value
    isNeg = value < 0
    value = abs(value)
    numList = list()
    newReverseNumber = 0
    while value > 0:
        k = value % 10
        newReverseNumber = newReverseNumber * 10 + k
        value //= 10
    
    if newReverseNumber >= 2**31 or newReverseNumber >= 2**31 - 1:
        return 0

    return newReverseNumber if not isNeg else -newReverseNumber


print(reverseIntegerByList(-123))