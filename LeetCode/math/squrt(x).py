



def mySqrt(num):
    if num == 0 or num == 1:
        return num
    
    left, right = 0, num
    output = 0
    while left <= right:
        mid = (left + right) // 2
    
        if (mid * mid) == num:
            return mid
        elif mid * mid > num:
            right = mid - 1
        else:
            left = mid + 1
            output = mid
            
        
    return output


print(mySqrt(8))