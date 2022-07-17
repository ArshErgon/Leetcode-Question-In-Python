



def checkPerfectNumber(num):
    runningSum = 0

    for i in range(1, num + 1):
        # runningSum += i if ((num // i) % 2 == 0) else 0
        if (num % i) == 0:
            runningSum += i
        if runningSum == num:
            return True
            
    return runningSum == num


print(checkPerfectNumber(2016))