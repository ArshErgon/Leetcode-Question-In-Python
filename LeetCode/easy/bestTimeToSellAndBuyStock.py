


# O(N) || O(1)
def bestTimeToBuyAndStockWithOptimal(array):
    if not array:
        return 0
    minVal = array[0]
    maxVal = float('-inf')
    for i in range(1, len(array)):
        maxVal = max(maxVal, array[i] - minVal)
        minVal = min(minVal, array[i])

    return maxVal if maxVal > 0 else 0


# O(N^2) || O(1)
def bestTimeToBuyAndStockWithTwoLoop(array):
    if not array:
        return 0

    maxProfit = float('-inf')

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            maxProfit = max(maxProfit, array[j] - array[i])

    return maxProfit if maxProfit > 0 else 0


l = [7,1,5,3,6,4]
l2 = [7,6,4,3,1]
# print(bestTimeToBuyAndStockWithTwoLoop(l))
# print(bestTimeToBuyAndStockWithTwoLoop(l2))
print(bestTimeToBuyAndStockWithOptimal(l))