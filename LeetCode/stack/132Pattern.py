



def find132pattern(nums):
    monoTonicStack = []
    minLeft = nums[0]
    
    for n in nums[1:]:
        while monoTonicStack and monoTonicStack[-1][0] <= n:
            monoTonicStack.pop()
            
        if monoTonicStack and monoTonicStack[-1][1] < n:
            return True
        
        monoTonicStack.append([n, minLeft])
        minLeft = min(minLeft, n)
    
    return False
        

print(find132pattern([3,1,4,2]))