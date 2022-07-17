





def combinationSum(candidates, target):
    
    result = []
    hashMap = {i:i for i in candidates}
    for c in candidates:
        secondSum = []
        isEmpty = False
        runningSum = c
        secondSum.append(c)
        for i in candidates:
            if (target - runningSum) in hashMap:
                secondSum.append(hashMap[target - runningSum])
                runningSum += hashMap[target - runningSum]
            
            if runningSum > target:
                break
            
            if runningSum == target and sum(secondSum) == target:
                isEmpty = True
                break

            elif (target - runningSum) not in hashMap:
                runningSum += c
                secondSum.append(c)
            else:
                runningSum += c
                secondSum.append(c)
            
        if isEmpty:
            result.append(secondSum)

    
    return result



candidates = [2,3,5]
target = 8

print(combinationSum(candidates, target))


