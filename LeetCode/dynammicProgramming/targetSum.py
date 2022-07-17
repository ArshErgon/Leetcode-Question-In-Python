


# O(n*t) where n is number of nodes and t is total
def targetSum(array, target):
    cache = {}

    return backTrack(array, target, 0, 0, cache)

def backTrack(array, target, index, total, cache):
    if index == len(array):
        return 1 if total == target else 0
    
    if (index, total) in cache:
        return cache[(index, total)]

    cache[(index, total)] = (
        backTrack(array, target, index + 1, total + array[index], cache) + 
        backTrack(array, target, index + 1, total - array[index], cache)
    )

    return cache[(index, total)]



nums = [1,1,1,1,1]
target = 3

print(targetSum(nums, target))