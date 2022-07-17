



def contingoursnums(nums):
    Map = {0:-1}
    count = 0
    result = 0
    for idx, num in enumerate(nums):
        if num == 0:
            count -= 1
        else:
            count += 1

        
        if count in Map:
            print(idx, Map[count])
            result = max(result, idx - Map[count])
        else:
            Map[count] = idx

    
    return result




nums = [1,1,1,0,0,0,1,1]
print(contingoursnums(nums))