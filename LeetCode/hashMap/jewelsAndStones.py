


def jewelsAndStones(jewels, stones):
    jewelsMap = dict()
    for i in jewels:
        jewelsMap[i] = jewelsMap.get(i, 0) + 1

    oldSum = sum(jewelsMap.values())

    for i in stones:
        if i in jewelsMap:
            jewelsMap[i] = jewelsMap.get(i, 0) + 1
    

    return sum(jewelsMap.values()) - oldSum



print(jewelsAndStones("aA", "aAAbbbb"))