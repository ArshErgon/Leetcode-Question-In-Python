





def minimumTimeDifference(timePoints):
    timeSeen = [False] * (24 * 60)
    for time in timePoints:
        HH, MM = time.split(':')
        seenFormula = (int(HH) * 60) + int(MM)
        if timeSeen[seenFormula]:
            return 0
        timeSeen[seenFormula] = True

    firstSeen = None
    secondSeen = None
    minVal = float('inf')

    for i in range(len(timeSeen)):
        if timeSeen[i]:
            if firstSeen == None:
                firstSeen = i
                secondSeen = i
            else:
                minVal = min(minVal, min(i - secondSeen, 1440 - i + secondSeen))
                secondSeen = i

    minVal = min(minVal, min(secondSeen - firstSeen, 1440 - secondSeen + firstSeen))
    
    return minVal

timePoints = ["23:59","00:00"]
# timePoints = ["00:00","23:59","00:00"]
print(minimumTimeDifference(timePoints))