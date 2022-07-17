



def sumOfEvenNumbersAfterQueries(nums, queries):
    totalEvenNumSum = sum([num  for num in nums if num % 2 == 0])
    result = []

    for val, idx in queries:
        oldVal = nums[idx]
        nums[idx] += val
        
        
        if oldVal % 2 == 0:
            totalEvenNumSum -= oldVal
        
        if nums[idx] % 2 == 0:
            totalEvenNumSum += nums[idx]
            
    
        result.append(totalEvenNumSum)            
    
    return result


print(sumOfEvenNumbersAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))
