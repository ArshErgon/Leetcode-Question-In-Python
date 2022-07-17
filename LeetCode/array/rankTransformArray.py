




def transformArray(array):
    newSortedArray = (sorted(set(array)))   
    indexMap = {val:idx+1 for idx, val in enumerate(newSortedArray)}


    # for idx, val in enumerate(newSortedArray):
    #     indexMap[val] = idx + 1

    
    return list(map(indexMap.get, array))


arr = [40,10,20,30]

print(transformArray(arr))
