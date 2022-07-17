

# O(N) || O(1)

def climbingStairs(n):
    if n <= 2:
        return n
    prevStep, nextStep = 1, 2

    for i in range(3, n + 1): 
        prevStep, nextStep = nextStep, prevStep + nextStep
    
    return nextStep


print(climbingStairs(4))