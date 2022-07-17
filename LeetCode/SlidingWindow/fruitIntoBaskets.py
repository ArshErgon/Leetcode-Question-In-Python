

# O(n) || O(1)
def fruitInBasket(fruits):
    prevFruit, secondLastFruit = -1, -1
    lastFruitCount = 0
    currMax = 0
    maxVal = 0

    for fruit in fruits:
        if fruit == prevFruit or fruit == secondLastFruit:
            currMax += 1
        else:
            currMax = lastFruitCount + 1
        
        if fruit == prevFruit:
            lastFruitCount += 1
        else:
            lastFruitCount = 1

        if fruit != prevFruit:
            secondLastFruit = prevFruit
            prevFruit = fruit

        maxVal = max(maxVal, currMax)

    return maxVal

print(fruitInBasket([1,2,3,2,2]))