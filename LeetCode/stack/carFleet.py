

# O(nlogn) || O(n)


def carFleet(target, pos, speed):
    stack = []

    for p, v in sorted(zip(pos, speed))[::-1]:
        difference = target - p
        mathEquation = difference / v
        if not stack: stack.append(mathEquation)
        elif mathEquation > stack[-1]:
            stack.append(mathEquation)

    return len(stack)


# print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
# print(carFleet(10, [10], [3]))
print(carFleet(100, [0, 2,4], [4,2,1]))