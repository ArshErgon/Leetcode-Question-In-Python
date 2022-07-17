

def sortColors(colors):
    if not colors or len(colors) <= 1:
        return colors
    
    orderFirst = 0
    orderSec = 1

    firstIdx, secIdx, thirdIdx = 0, 0, len(colors) - 1

    while secIdx <= thirdIdx:
        ele = colors[secIdx]
        
        if ele == orderFirst:
            colors[firstIdx], colors[secIdx] = colors[secIdx], colors[firstIdx]
            firstIdx += 1
            secIdx += 1
        elif ele == orderSec:
            secIdx += 1
        else:
            colors[thirdIdx], colors[secIdx] = colors[secIdx], colors[thirdIdx]
            thirdIdx -= 1
    return colors
    


print(sortColors([2,0,2,1,1,0]))