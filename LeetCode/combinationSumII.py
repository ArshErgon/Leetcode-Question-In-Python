




def combinationSumII(candidates, target):
    candidates.sort()
    result = list()
    
    combination(0, target, result, [])
    return result

global prevCan
prevCan = None

def combination(idx, target, result, path):
    global prevCan
    if target < 0:
        return 
    
    if target == 0:
        result.append(path)
        return

    if idx == len(candidates):
        return 

    for i in range(idx, len(candidates)):
        if i > idx and candidates[i] == candidates[i - 1]:
            continue
        combination(i + 1, target - candidates[i], result, path + [candidates[i]])



candidates = [10,1,2,7,6,1,5]
target = 8

print(combinationSumII(candidates, target))