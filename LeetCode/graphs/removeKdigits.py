

from regex import R


def removeKDigits(nums, k):
    if not k:return nums
    monoTonicStack = []

    for i in nums:
        while monoTonicStack and monoTonicStack[-1] > i and k:
            monoTonicStack.pop()
            k -= 1

        monoTonicStack.append(i)

    newNum = "".join(monoTonicStack[:len(monoTonicStack)-k])

    return str(int(newNum)) if newNum else "0"

print(removeKDigits("10200", 1))