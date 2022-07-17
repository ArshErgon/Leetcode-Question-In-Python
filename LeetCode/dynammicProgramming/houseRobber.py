




def houseRobber(houses):
    if not houses:
        return 0

    rob1, rob2 = 0, 0
    for i in range(len(houses)):
        temp = max(rob1 + houses[i], rob2)
        rob1 = rob2
        rob2 = temp
    
    return rob2


print(houseRobber([2,7,9,3,1]))