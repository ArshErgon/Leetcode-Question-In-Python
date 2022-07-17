


# O(n) || O(1)
def distanceBetweenBustop(distance, start, destination):
    clockWiseDirection = 0
    totalSum = 0

    for idx, val in enumerate(distance):
        if start < destination and (idx >= start and idx < destination ):
            clockWiseDirection += val
        
        if start > destination and (idx >= start or idx < destination ):
            clockWiseDirection += val

        totalSum += val

    return min(clockWiseDirection, totalSum-clockWiseDirection)


print(distanceBetweenBustop([1,2,3,4], 0, 2))