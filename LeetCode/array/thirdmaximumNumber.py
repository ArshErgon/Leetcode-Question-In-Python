



def thirdMaximumNumber(nums):
    if not nums:
        return nums
    threeLargest = [None] * 3
    for num in nums:
        updateThreeMax(threeLargest, num)

    return threeLargest[2]


def updateThreeMax(threeLargest, num):
    if threeLargest[2] is None or threeLargest[2] < num:
        shiftUp(threeLargest, num, 2)
    elif threeLargest[1] is None or threeLargest[1] < num:
        shiftUp(threeLargest, num, 1)
    elif threeLargest[0] is None or threeLargest[0] < num:
        shiftUp(threeLargest, num, 0)


def shiftUp(threeLargest, num, idx):
    for i in range(idx + 1):
        if i == idx: 
            threeLargest[i] = num
        else:
            threeLargest[i] = threeLargest[i + 1]


    

nums = [3,2,1]

print(thirdMaximumNumber(nums))

