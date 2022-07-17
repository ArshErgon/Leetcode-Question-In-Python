


def dividingNumbers(left, right):
    if not left and not right:
        return []
    numberRange = list(range(left, right + 1))
    result = []
    for i in numberRange:
        flag = True
        copy = i
        while copy != 0:
            num = copy % 10
            if num == 0 or i % num != 0:
                flag = False
                break
            copy //= 10
        if flag:
            result.append(i)

    return result
    

print(dividingNumbers(1, 22))